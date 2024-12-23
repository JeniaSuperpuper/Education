import React from 'react';
import lupazapupupupazalupu from "../assets/images/ZA-loop'a.svg"

export default function CatalogSearch () {
    return (
    <>
                    <div className="catalog__filter">
                        <button>All Courses</button>
                        <button>Math</button>
                        <button>Literature</button>
                        <button>English</button>
                        <button>Art</button>
                    </div>
                    <div className="catalog__ss-wrapper">
                        <div className="catalog__search">
                            <input type="search" placeholder='Serach Course, Teacher name' />
                            <button type='submit'><img src={lupazapupupupazalupu} alt="search" /></button>
                        </div>
                        <div className="catalog__sort">
                            <label htmlFor="select">Sort by:</label>
                            <select name="" id="select" >
                                <option value="">Latest</option>
                            </select>
                        </div>
                    </div>
    </>
    )
}