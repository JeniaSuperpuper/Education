import  { useEffect } from "react";

const Modal = ({ active, setActive, children }) => {
  const handleKeyDown = (e) => {
    if (e.key === "Escape") {
      setActive(false);
    }
  };

  useEffect(() => {
    if (active) {
      window.addEventListener("keydown", handleKeyDown);
    }
    return () => {
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, [active]); 

  return (
    <div className={active ? "modal active" : "modal"}>
      <div
        className={active ? "modal__content active" : "modal__content"}
        onClick={(e) => e.stopPropagation()}
      >
        <p className="modal__close-btn" onClick={() => setActive(false)}>
        &#x2715;
        </p>
        {children}
      </div>
    </div>
  );
};

export default Modal;
