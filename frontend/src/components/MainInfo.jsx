import boy from "../assets/images/school_boy.png"
import check from "../assets/images/check.svg"

export default function Lessons() {
  return (
    <>
    <div className="container">
        <div className="main-info__wrap">
            <img src={boy} alt="boy" />
            <div className="main-info__block">
                <p className="main-info__title">
                What will your child get after studying at Edudu?
                </p>
                <p className="main-info__text"><img src={check} alt="check" />Master program knowledge at school</p>
                <p className="main-info__text"><img src={check} alt="check" />The ability to criticize knowledge increases    </p>
                <p className="main-info__text"><img src={check} alt="check" />Respond confidently when encountering difficult situations</p>
            </div>
        </div>
    </div>
    </>
  );
}
