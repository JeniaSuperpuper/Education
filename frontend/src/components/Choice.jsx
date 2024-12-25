import kopilka from "../assets/images/kopilka.svg";
import teacher from "../assets/images/teacher.svg";
import kniga from "../assets/images/kniga.svg";

export default function Choice() {
  return (
    <section className="choice">
      <div className="choice__wrap">
        <div className="choice__container">
          <div className="choice__head">
            <h1 className="choice__head-text">Why should you choose Edudu?</h1>
          </div>
            <div className="choice__cards">
              <div className="choice__card">
                <div className="choice__card-img">
                  <img
                    src={teacher}
                    alt="учитель "
                    className="choice__card-img"
                  />
                </div>
                <div className="choice__card-allText">
                <div className="choice__card-text">Experienced teacher</div>
                <div className="choice__card-paragraph">
                  Instructors from all over Vietnam and around the world,
                  providing quality learning experiences and helping students
                  develop their full potential
                </div>
                </div>  
              </div>
              <div className="choice__card">
                <div className="choice__card-img">
                  <img src={kniga} alt="книга" className="choice__card-img" />
                </div>
                <div className="choice__card-allText">
                <div className="choice__card-text">Creative program</div>
                <div className="choice__card-paragraph">
                  Flexible payment, suitable to personal financial situation and
                  study schedule. Pay monthly, by course or “study now, pay
                  later”
                </div>
                </div>
              </div>
              <div className="choice__card">
                <div className="choice__card-img">
                  <img
                    src={kopilka}
                    alt="копилка"
                    className="choice__card-img"
                  />
                </div>
                <div className="choice__card-allText">
                <div className="choice__card-text">Appropriate cost</div>
                <div className="choice__card-paragraph">
                  Thiết kế giáo trình dựa trên năng lực và nhu cầu từng học
                  viên, hoạt động học tập hấp dẫn, tương tác 2 chiều liên tục.
                </div>
                </div>
              </div>
            </div>
        </div>
      </div>
    </section>
  );
}
