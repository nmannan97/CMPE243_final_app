import React from 'react'

export default class AutoCompleteText extends React.Component{
    constructor(props){
        super(props);
        this.items = [
            'item 1',
            'iteam 2',
        ];
        this.state = {
            suggestions: [],
        };
    }

    onTextChanged = (e) => {
        const value = e.target.value;
        let suggestions = [];
        if(value.length > 0){
            const regex = new RegExp(`^${value}`, 'i')
            const suggestions = this.items.sort().filter(v => v.test(regex));
        }
        this.setState(()=> ({suggestions}));

    
    }
    renderSuggestions () {
        const{suggestions} = this.state;
        if(suggestions === 0){
            return null;
        }
        return (
            <ul>
                {this.suggestions.map((item)=> <li>(item)</li>)}
            </ul>
        )
    }
    render() {
        return(
            <div>
                <input onChange= {this.onTextChanged} type = "text"/>
                    {this.renderSuggestions}

            </div>
        )
    }
}