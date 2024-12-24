import React, { useEffect, useState } from 'react';
import lupazapupupupazalupu from "../assets/images/ZA-loop'a.svg";

export default function CatalogSearch() {
    const [categories, setCategories] = useState([]); // Список категорий
    const [selectedCategory, setSelectedCategory] = useState(null); // Выбранная категория
    const [coursesByCategory, setCoursesByCategory] = useState({}); // Курсы для каждой категории

    // Получение списка категорий
    useEffect(() => {
        const fetchCategories = async () => {
            try {
                const response = await fetch('http://localhost:8000/api/v1/courses/category');
                if (!response.ok) {
                    throw new Error('Failed to fetch categories');
                }
                const data = await response.json();
                setCategories(data); // Сохраняем категории

                // Загружаем курсы для каждой категории
                data.forEach((category) => {
                    fetchCoursesForCategory(category.slug);
                });
            } catch (error) {
                console.error('Error fetching categories:', error);
            }
        };

        fetchCategories();
    }, []);

    // Получение курсов для конкретной категории
    const fetchCoursesForCategory = async (slug) => {
        try {
            const response = await fetch(`http://localhost:8000/api/v1/courses/category/${slug}/courses`);
            if (!response.ok) {
                throw new Error('Failed to fetch courses');
            }
            const data = await response.json();
            setCoursesByCategory((prev) => ({
                ...prev,
                [slug]: data, // Сохраняем курсы для категории по её slug
            }));
        } catch (error) {
            console.error(`Error fetching courses for category ${slug}:`, error);
        }
    };

    // Обработчик нажатия на кнопку категории
    const handleCategoryClick = (category) => {
        setSelectedCategory(category.id === selectedCategory?.id ? null : category); // Переключаем выбранную категорию
    };

    return (
        <>
            <div className="catalog__filter">
                <button className='catalog__filter-all' onClick={() => setSelectedCategory(null)}>All Courses</button>
                {categories.map((category) => (
                    <button
                        key={category.id}
                        onClick={() => handleCategoryClick(category)}
                        className={selectedCategory?.id === category.id ? 'active' : ''}
                    >
                        {category.title}
                    </button>
                ))}
            </div>
            <div className="catalog__ss-wrapper">
                <div className="catalog__search">
                    <input type="search" placeholder='Search Course, Teacher name' />
                    <button type='submit'><img src={lupazapupupupazalupu} alt="search" /></button>
                </div>
                <div className="catalog__sort">
                    <label htmlFor="select">Sort by:</label>
                    <select name="" id="select">
                        <option value="">Latest</option>
                    </select>
                </div>
            </div>
            <div className="catalog__card-block">
                {selectedCategory ? (
                    // Если выбрана категория, показываем её курсы
                    <div className="catalog__card-wrapper">
                        {coursesByCategory[selectedCategory.slug]?.map((course) => (
                            <div key={course.id} className="catalog__card">
                                <img src={course.image} alt="img" />
                                <h3>{course.title}</h3>
                                <p>{course.description}</p>
                                <h4>{course.price}</h4>
                            </div>
                        ))}
                    </div>
                ) : (
                    
                    // Если категория не выбрана, показываем все курсы из всех категорий
                    categories.map((category) => (
                        <div className='catalog__card-block' key={category.id}>
                            <h2>{category.title}</h2>
                            <div className="catalog__card-wrapper">
                            {coursesByCategory[category.slug]?.map((course) => (
                                    <div className='catalog__card' key={course.id}>
                                        <img src={course.image} alt="img" />
                                        <h3>{course.title}</h3>
                                        <p>{course.description}</p>
                                        <h4>{course.price}</h4>
                                    </div>
                            ))}
                            </div>
                        </div>
                    ))
                )}
            </div>
        </>
    );
}