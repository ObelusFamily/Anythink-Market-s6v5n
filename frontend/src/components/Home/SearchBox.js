import React from "react"
import agent from '../../agent';

const SearchBox = () => {
    return (
        <div>
            <input
                id="search-box"
                placeholder="What is it that you truly desire?"
                onInput={(ev) => {
                    const value = ev.target.value;
                    if (value.length >= 3) agent.Items.byTitle(value);
                }} />
        </div>
    )    
}

export default SearchBox;