import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import Button from '@mui/material/Button';

function Recipes() {
    const [recipes, setRecipes] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/api/recipes')
            .then(response => response.json())
            .then(data => setRecipes(data))
            .catch(error => console.error('Error fetching recipes:', error));
    }, []);
    const linkStyle = {
        padding: '10px',
    };
    return (
        <div>
            {recipes.length > 0 ? (
                recipes.map(recipe => (
                    <div style={linkStyle}>
                        <Link key={recipe.recipe_id} to={`/recipes/${recipe.recipe_id}`}>
                            <Button variant="contained">{recipe.recipe_name}</Button>
                        </Link>
                    </div>
                ))
            ) : (
                <p>No recipes!</p>
            )}
        </div>
    );
}

export default Recipes;
