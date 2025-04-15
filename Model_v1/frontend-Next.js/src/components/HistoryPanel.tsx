// src/components/HistoryPanel.tsx
import { motion } from "framer-motion"; // Add this line
import { Trash2, Download } from "lucide-react";

const HistoryPanel = ({ history, exportHistoryAsCSV, clearHistory, deletePrompt, handleHistoryClick }) => (
  <motion.div
    initial={{ x: -250 }}
    animate={{ x: 0 }}
    exit={{ x: -250 }}
    transition={{ duration: 0.3 }}
    className="w-80 bg-gray-900 border-r border-gray-700 p-6 shadow-lg flex flex-col h-full"
  >
    <div className="flex justify-between items-center mb-4">
      <h2 className="text-lg font-bold text-white">History</h2>
      <div className="flex gap-2">
        <button onClick={exportHistoryAsCSV} className="text-green-500">
          <Download className="w-5 h-5" />
        </button>
        <button onClick={clearHistory} className="text-red-500" aria-label="Clear History">
          <Trash2 className="w-5 h-5" />
        </button>
      </div>
    </div>

    <div className="flex-1 overflow-y-auto space-y-2">
      {history.length > 0 ? (
        history.map((item) => (
          <div
            key={item.id}
            className="bg-gray-800 border border-gray-700 p-4 rounded-lg flex justify-between items-center text-white cursor-pointer"
            onClick={() => handleHistoryClick(item)}
          >
            <span className="truncate max-w-[180px]">{item.text}</span>
            <span className="text-sm text-gray-400">{item.classification}</span>
            <button
              onClick={(e) => {
                e.stopPropagation();
                deletePrompt(item.id);
              }}
              className="ml-2 text-red-500 hover:text-red-700"
            >
              <Trash2 className="w-5 h-5" />
            </button>
          </div>
        ))
      ) : (
        <div className="text-gray-500">No history available</div>
      )}
    </div>
  </motion.div>
);

export default HistoryPanel;
