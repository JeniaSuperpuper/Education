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

    const [query, setQuery] = useState('');
const [results, setResults] = useState([]);

const handleSearch = async () => {
  try {
    const response = await fetch(`http://127.0.0.1:8000/api/v1/courses/search/?search=${query}`);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    setResults(data);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};

    return (
        <>
            <div className="catalog__filter">
                <button onClick={() => setSelectedCategory(null)}>All Courses</button>
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
                    <input
                        type="search"
                        placeholder="Search Course"
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                    />
                    <button onClick={handleSearch}><img src={lupazapupupupazalupu} alt="search" /></button>

                    <ul>
                        {results.map((item) => (
                        <li key={item.id}>
                            {item.name} - {item.description}
                        </li>
                        ))}
                    </ul>
                </div>
                <div className="catalog__sort">
                    <label htmlFor="select">Sort by:</label>
                    <select name="" id="select">
                        <option value="">Latest</option>
                    </select>
                </div>
            </div>
            <div className="catalog__courses">
                {selectedCategory ? (
                    // Если выбрана категория, показываем её курсы
                    coursesByCategory[selectedCategory.slug]?.map((course) => (
                        <div key={course.id} className="catalog__course">
                            <h3>{course.title}</h3>
                            <p>{course.description}</p>
                        </div>
                    ))
                ) : (
                    // Если категория не выбрана, показываем все курсы из всех категорий
                    categories.map((category) => (
                        <div key={category.id}>
                            <h2>{category.title}</h2>
                            {coursesByCategory[category.slug]?.map((course) => (
                                <div key={course.id} className="catalog__course">
                                    <h3>{course.title}</h3>
                                    <p>{course.description}</p>
                                </div>
                            ))}
                        </div>
                    ))
                )}
            </div>
        </>
    );
}