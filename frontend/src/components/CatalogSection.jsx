import image from '../assets/images/Catalog_image.png'

export default function Catalog () {
    return (
        <section className="catalog">
            <div className="container">
                <div className="catalog__wrapper">
                    <div className="catalog__navigation">
                        <button>Home</button>
                        <p>|</p>
                        <button>Pricing</button>
                    </div>
                    <div className="catalog__banner">
                        <div className="catalog__banner-text">
                            <h1>Edudu offers you a 30% discount this season</h1>
                            <p>Promotion valid from May 1, 2023 - June 30, 2023</p>
                            <button>Explore now</button>
                        </div>
                        <div className="catalog__banner-image">
                            <img src={image} alt="img" />
                        </div>
                    </div>
                </div>
            </div>
        </section>
    )
}