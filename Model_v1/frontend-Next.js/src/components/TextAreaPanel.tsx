import { useEffect, useRef, useState } from "react";
import { motion } from "framer-motion";
import { Trash2 } from "lucide-react";

interface TextAreaPanelProps {
  text: string;
  setText: (v: string) => void;
  classifyText: () => void;
  result: string | null;
  loading: boolean;
  errorMessage: string;
  editMessage: string;
}

const TextAreaPanel: React.FC<TextAreaPanelProps> = ({
  text,
  setText,
  classifyText,
  result,
  loading,
  errorMessage,
  editMessage,
}) => {
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const [focused, setFocused] = useState(false);

  // Auto-focus on mount
  useEffect(() => {
    textareaRef.current?.focus();
  }, []);

  // Decide label position based on focus or content
  const labelClass = `
    absolute left-4 transition-all text-gray-500 pointer-events-none
    ${focused || text ? "top-2 text-sm" : "top-6 text-base"}
  `;

  // State for handling placeholder visibility
  const [showPlaceholder, setShowPlaceholder] = useState(true);

  // Effect to hide placeholder when user types
  useEffect(() => {
    if (text) {
      setShowPlaceholder(false);
    } else {
      setShowPlaceholder(true);
    }
  }, [text]);

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="flex-1 flex items-center justify-center p-6 h-full overflow-auto"
    >
      <div className="w-full max-w-2xl bg-gradient-to-br from-gray-700 via-gray-900 to-black p-1 rounded-2xl shadow-2xl">
        <div className="bg-gray-900 p-6 rounded-xl relative">

          {/* textarea + floating label + clear button */}
          <div className="relative mb-6">
            <textarea
              ref={textareaRef}
              value={text}
              onChange={(e) => setText(e.target.value)}
              rows={6}
              onFocus={() => setFocused(true)}
              onBlur={() => setFocused(false)}
              className="w-full bg-transparent text-white p-8 resize-none rounded-lg
                         focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
            />
            {showPlaceholder && (
              <label className={labelClass}>
                Paste email text here…
              </label>
            )}

            {text && (
              <button
                onClick={() => setText("")}
                className="absolute top-3 right-5 text-gray-400 hover:text-gray-200 transition"
                aria-label="Clear Input"
              >
                <Trash2 className="w-5 h-5" />
              </button>
            )}

            {errorMessage && (
              <p className="mt-2 text-sm text-red-400 flex items-center gap-1">
                <Trash2 className="w-4 h-4" /> {errorMessage}
              </p>
            )}
            {editMessage && (
              <p className="mt-2 text-sm text-green-400">{editMessage}</p>
            )}
          </div>

          {/* classify button */}
          <motion.button
            onClick={classifyText}
            disabled={loading}
            whileTap={{ scale: 0.95 }}
            whileHover={{ scale: 1.02 }}
            className="w-full py-3 bg-blue-600 hover:bg-blue-700 active:bg-blue-800
                       text-white font-semibold rounded-lg shadow-md transition-all
                       disabled:opacity-50"
          >
            {loading ? <span className="animate-pulse">Classifying...</span> : "Classify"}
          </motion.button>

          {/* simple in‑panel result */}
          {result && (
            <div className="mt-6 bg-gray-800 p-4 rounded-md text-white">
              <p className="font-medium">Result:</p>
              <p className="text-xl font-bold">{result}</p>
            </div>
          )}
        </div>
      </div>
    </motion.div>
  );
};

export default TextAreaPanel;
