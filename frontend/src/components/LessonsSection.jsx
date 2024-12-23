import art from "../assets/images/Art.svg";
import literature from "../assets/images/Literature.svg";
import math from "../assets/images/Math.svg";
import english from "../assets/images/English.svg";

export default function Lessons() {
  return (
    <section className="lessons">
      <div className="lessons__wrap">
        <div className="lessons__container">
          <div className="lessons__text">
            <h3 className="lessons__mainText">
              Lessons revolve around 4 areas
            </h3>
            <p className="lessons__paragraph">
              Diverse lessons around 4 subjects: Math, literature, English,
              drawing help children improve their comprehensive knowledge
            </p>
          </div>
          <div className="lessons__items">
            <button className="lessons__item">
              <img src={math} alt="" />
              <h2 className="lessons__item-text">Math</h2>
            </button>
            <button className="lessons__item">
              <img src={literature} alt="" />
              <h2 className="lessons__item-text">Lit Energy</h2>
            </button>
            <button className="lessons__item">
              <img src={english} alt="" />
              <h2 className="lessons__item-text">English</h2>
            </button>
            <button className="lessons__item">
              <img src={art} alt="" />
              <h2 className="lessons__item-text">Art</h2>
            </button>
          </div>
        </div>
      </div>
    </section>
  );
}