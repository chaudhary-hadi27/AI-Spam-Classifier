// src/app/page.tsx

"use client";

import { useState, useEffect, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { History, Mail, Trash2, Sun, Moon, Download } from "lucide-react";
import Papa from "papaparse";
import HistoryPanel from "../components/HistoryPanel";
import TextAreaPanel from "../components/TextAreaPanel";

export default function Home() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [historyOpen, setHistoryOpen] = useState(false);
  const [history, setHistory] = useState([]);
  const [contactOptions, setContactOptions] = useState(false);
  const [editMessage, setEditMessage] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [darkMode, setDarkMode] = useState(true);
  const historyRef = useRef(null);

  const classifyText = async () => {
    if (!text.trim()) {
      setErrorMessage("Please enter some text to classify.");
      return;
    }

    const trimmedText = text.trim();

    if (history.some((entry) => entry.text === trimmedText)) {
      setErrorMessage("This text already exists in history.");
      return;
    }

    setLoading(true);
    setResult(null);
    setErrorMessage("");
    setEditMessage("");

    setTimeout(() => {
      const isSpam = Math.random() > 0.5;
      const classification = isSpam ? "Spam" : "Ham";
      setResult(classification);

      fetch("http://localhost:8000/api/savePrompt", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: trimmedText, classification }),
      })
        .then((res) => res.json())
        .then(() => {
          const newItem = {
            id: Date.now(),
            text: trimmedText,
            classification,
          };
          setHistory((prev) => [newItem, ...prev]);
          setEditMessage("Prompt has been added to history.");
          setText("");
          scrollToTop();
        })
        .catch((err) => {
          console.error("Error:", err);
          setErrorMessage("Failed to save prompt. Try again.");
        })
        .finally(() => setLoading(false));
    }, 1500);
  };

  const scrollToTop = () => {
    if (historyRef.current) {
      historyRef.current.scrollTop = 0;
    }
  };

  const loadHistory = () => {
    fetch("http://localhost:8000/api/getPrompts")
      .then((res) => res.json())
      .then((data) => setHistory(data.reverse()))
      .catch((err) => console.error("Error loading history:", err));
  };

  const deletePrompt = (id) => {
    fetch(`http://localhost:8000/api/deletePrompt/${id}`, {
      method: "DELETE",
    })
      .then((res) => res.json())
      .then(() => {
        setHistory((prev) => prev.filter((item) => item.id !== id));
        setEditMessage("Prompt deleted.");
      })
      .catch((err) => {
        console.error("Error deleting prompt:", err);
        setErrorMessage("Failed to delete prompt.");
      });
  };

  const clearHistory = () => {
    if (!window.confirm("Are you sure you want to delete all history?")) return;

    fetch("http://localhost:8000/api/clearPrompts", {
      method: "DELETE",
    })
      .then((res) => res.json())
      .then(() => {
        setHistory([]);
        setEditMessage("History has been cleared.");
      })
      .catch((err) => {
        console.error("Error clearing history:", err);
        setErrorMessage("Failed to clear history.");
      });
  };

  const openMail = (type = "web") => {
    const email = "chaudharyhadi27@gmail.com";
    const subject = "Inquiry";
    const body = "Hello, I would like to ask about...";

    const urls = {
      web: `https://mail.google.com/mail/?view=cm&fs=1&to=${email}&su=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`,
      outlook: `https://outlook.live.com/owa/?path=/mail/action/compose&to=${email}&subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`,
      app: `mailto:${email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`,
    };

    type === "app" ? (window.location.href = urls.app) : window.open(urls.web, "_blank") || window.open(urls.outlook, "_blank");

    setContactOptions(false);
  };

  const handleHistoryClick = (item) => {
    setText(item.text);
    setResult(item.classification);
    setEditMessage("History loaded.");
  };

  const toggleDarkMode = () => {
    setDarkMode((prevMode) => !prevMode);
  };

  const exportHistoryAsCSV = () => {
    const csv = Papa.unparse(history);
    const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
    const link = document.createElement("a");
    const url = URL.createObjectURL(blob);

    link.setAttribute("href", url);
    link.setAttribute("download", "history.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  useEffect(() => {
    loadHistory();
  }, []);

  const containerClasses = darkMode
    ? "min-h-screen h-screen flex flex-col bg-black text-white"
    : "min-h-screen h-screen flex flex-col bg-white text-black";

  return (
    <div className={containerClasses}>
      {/* Nav */}
      <nav className="w-full flex items-center justify-between p-4 bg-gray-900 border-b border-gray-700 text-white">
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 1 }} className="text-4xl font-extrabold bg-gradient-to-r from-gray-300 to-white bg-clip-text text-transparent">
          AI Email Classifier
        </motion.div>

        {/* Displaying Model_v1 in the navbar */}
        <motion.div
          className="text-xl font-semibold bg-gradient-to-r from-blue-500 to-green-400 bg-clip-text text-transparent"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1 }}
        >
          Model_v1
        </motion.div>

        <div className="flex gap-6 text-lg relative">
          <button className="hover:text-blue-400">Home</button>

          <button onClick={() => setHistoryOpen(!historyOpen)} className="hover:text-blue-400 flex items-center gap-1">
            <History className="w-5 h-5" /> History
          </button>

          <button onClick={() => setContactOptions(!contactOptions)} className="hover:text-blue-400 flex items-center gap-1 relative">
            <Mail className="w-5 h-5" /> Contact
          </button>

          {contactOptions && (
            <div className="absolute top-8 right-0 bg-gray-800 shadow-lg border border-gray-700 p-2 rounded-md z-10">
              <button onClick={() => openMail("web")} className="block w-full text-left px-4 py-2 hover:bg-gray-700">Open Web Mail</button>
              <button onClick={() => openMail("app")} className="block w-full text-left px-4 py-2 hover:bg-gray-700">Open Mail App</button>
            </div>
          )}

          <button onClick={toggleDarkMode} className="hover:text-yellow-400 flex items-center gap-1">
            {darkMode ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
          </button>
        </div>
      </nav>

      <div className="flex flex-1 overflow-hidden">
        <AnimatePresence>
          {historyOpen && (
            <HistoryPanel
              history={history}
              exportHistoryAsCSV={exportHistoryAsCSV}
              clearHistory={clearHistory}
              deletePrompt={deletePrompt}
              handleHistoryClick={handleHistoryClick}
            />
          )}
        </AnimatePresence>

        <TextAreaPanel
          text={text}
          setText={setText}
          classifyText={classifyText}
          result={result}
          loading={loading}
          errorMessage={errorMessage}
          editMessage={editMessage}
        />
      </div>
    </div>
  );
}
