import image from '../assets/images/Main_photo.png';

export default function Main() {
    return (
        <section className="main">
            <div className="container">
                <div className="main__wrapper">
                    <div className="main__title">
                        <h1>Knowledge Connection
                        <strong> Open the Door to the Future</strong></h1>
                        <p>Giving every student the opportunity to access the best education and open the door to the world of knowledge.
                        Start your learning journey today with Edudu to become an outstanding student in our learning community.</p>
                        <button>Get started !</button>
                    </div>
                    <div className="main__image">
                        <img src={image} alt="img" />
                    </div>
                </div>
            </div>
        </section>
    );
}