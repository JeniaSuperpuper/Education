import React, { useEffect, useState } from 'react';
import lupazapupupupazalupu from "../assets/images/ZA-loop'a.svg";

export default function CatalogSearch() {
    const [categories, setCategories] = useState([]); // Список категорий
    const [selectedCategory, setSelectedCategory] = useState(null); // Выбранная категория
    const [coursesByCategory, setCoursesByCategory] = useState({}); // Курсы для каждой категории
    const [searchQuery, setSearchQuery] = useState(''); // Состояние для поискового запроса
    const [sortBy, setSortBy] = useState(''); // Состояние для сортировки

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

<<<<<<< HEAD
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
=======
    // Обработчик изменения поискового запроса
    const handleSearchChange = (e) => {
        setSearchQuery(e.target.value);
    };

    // Обработчик изменения сортировки
    const handleSortChange = (e) => {
        const value = e.target.value;
        setSortBy(value === 'all' ? '' : value); // Сбрасываем сортировку, если выбрано "All courses"
    };

    // Функция фильтрации и сортировки
    const getFilteredAndSortedCourses = (courses) => {
        let filteredCourses = courses;

        // Фильтрация по поисковому запросу
        if (searchQuery) {
            filteredCourses = filteredCourses.filter((course) =>
                course.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                course.description.toLowerCase().includes(searchQuery.toLowerCase())
            );
        }

        // Сортировка (если выбрана)
        if (sortBy) {
            switch (sortBy) {
                case 'price-low-to-high':
                    filteredCourses.sort((a, b) => a.price - b.price);
                    break;
                case 'price-high-to-low':
                    filteredCourses.sort((a, b) => b.price - a.price);
                    break;
                default:
                    break;
            }
        }

        return filteredCourses;
    };
>>>>>>> 50140d915f5a21b0c5d8b6bf5d630a1851c5df0f

    return (
        <>
            <div className="catalog__filter">
                <button className='catalog__filter-all' onClick={() => setSelectedCategory(null)}>All Courses</button>
                {categories.map((category) => (
                    <button
                        key={category.id}
                        onClick={() => handleCategoryClick(category)}
                        className={selectedCategory?.id === category.id ? 'activeBtn' : ''}
                    >
                        {category.title}
                    </button>
                ))}
            </div>
            <div className="catalog__ss-wrapper">

                <div className="catalog__search">
                    <input
                        type="search"
<<<<<<< HEAD
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
=======
                        placeholder='Search Course, Teacher name'
                        value={searchQuery}
                        onChange={handleSearchChange}
                    />
                    <button type='submit'><img src={lupazapupupupazalupu} alt="search" /></button>
>>>>>>> 50140d915f5a21b0c5d8b6bf5d630a1851c5df0f
                </div>
                <div className="catalog__sort">
                    <label htmlFor="select">Sort by:</label>
                    <select name="" id="select" value={sortBy} onChange={handleSortChange}>
                        <option value="price-low-to-high">Price: Low to High</option>
                        <option value="price-high-to-low">Price: High to Low</option>
                    </select>
                </div>
            </div>
            <div className="catalog__card-block">
                {selectedCategory ? (
                    // Если выбрана категория, показываем её курсы
                    <div className="catalog__card-wrapper">
                        {getFilteredAndSortedCourses(coursesByCategory[selectedCategory.slug] || []).map((course) => (
                            <div key={course.id} className="catalog__card">
                                <img src={course.image} alt="img" />
                                <div className="catalog__card-desc">
                                    <h3>{(course.title.length >= 100) ? (course.title.slice(0, 100) + '...') : (course.title)}</h3>
                                    <p>{(course.description.length >= 100) ? (course.description.slice(0, 100) + '...') : (course.description)}</p>
                                </div>
                                <h4>$ {course.price}</h4>
                                <a href="">Read more</a>
                            </div>
                        ))}
                    </div>
                ) : (
                    // Если категория не выбрана, показываем все курсы из всех категорий
                    categories.map((category) => {
                        const courses = coursesByCategory[category.slug] || [];
                        const filteredCourses = getFilteredAndSortedCourses(courses);

                        // Не отображать категорию, если курсов нет после фильтрации
                        if (filteredCourses.length === 0) {
                            return null;
                        }

                        return (
                            <div className='catalog__card-block' key={category.id}>
                                <h2>{category.title} Course</h2>
                                <div className="catalog__card-wrapper">
                                    {filteredCourses.map((course) => (
                                        <div className='catalog__card' key={course.id}>
                                            <img src={course.image} alt="img" />
                                            <div className="catalog__card-desc">
                                                <h3>{(course.title.length >= 100) ? (course.title.slice(0, 100) + '...') : (course.title)}</h3>
                                                <p>{(course.description.length >= 100) ? (course.description.slice(0, 100) + '...') : (course.description)}</p>
                                            </div>
                                            <h4>$ {course.price}</h4>
                                            <a href="">Read more</a>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        );
                    })
                )}
            </div>
        </>
    );
}