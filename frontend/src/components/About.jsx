import child from "../assets/images/backtoschool.svg";
import checkbox from "../assets/images/Checkbox.svg";

export default function About() {
  return (
    <section className="about">
      <div className="about__wrap">
        <div className="about__container">
          <div className="about__box-image">
            <img src={child} alt="child" className="about__image" />
          </div>
          <div className="about__text">
            <div className="about__mainText">
              <h3 className="about__mainText-text">
                What will your child get after studying at Edudu?
              </h3>
            </div>
            <div className="about__paragraphes">
              <p className="about__paragraph-text">
                {" "}
                <img
                  src={checkbox}
                  alt="checkbox"
                  className="about__checkbox"
                />{" "}
                Master program knowledge at school
              </p>
              <p className="about__paragraph-text">
                <img
                  src={checkbox}
                  alt="checkbox"
                  className="about__checkbox"
                />
                The ability to criticize knowledge increases
              </p>
              <p className="about__paragraph-text">
                <img
                  src={checkbox}
                  alt="checkbox"
                  className="about__checkbox"
                />
                Respond confidently when encountering difficult situations
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
