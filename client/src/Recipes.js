import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

function Recipes() {
    const [recipes, setRecipes] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/api/recipes')
            .then(response => response.json())
            .then(data => setRecipes(data))
            .catch(error => console.error('Error fetching recipes:', error));
    }, []);

    return (
        <div>
            <h1>Home Page</h1>
            {recipes.length > 0 ? (
                recipes.map(recipe => (
                    <Link key={recipe.recipe_id} to={`/recipes/${recipe.recipe_id}`}>
                        <button>{recipe.recipe_name}</button>
                    </Link>
                ))
            ) : (
                <p>No recipes!</p>
            )}
        </div>
    );
}

export default Recipes;
