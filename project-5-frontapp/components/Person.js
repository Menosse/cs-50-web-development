import React, {Component} from 'react';

class Person extends Component {
    constructor() {
        super();
        this.state = {
            user: [],
            isLoading: false,
            error: null
        }
    }

    componentDidMount() {
        this.setState({ isLoading: true });
        this.fetchRandomUser();        
    }

    fetchRandomUser = async() => {
        try {
            await fetch('https://randomuser.me/api/')
            .then(results => {
                return results.json();
            })
            .then(data => {
                let user = data.results.map((user) => {
                    let userElm = '';
                    
                    if (typeof user !== undefined && typeof user.name !== undefined && typeof user.picture != undefined) {
                        userElm = <div key={user}>
                            <h2>{user.name.first} {user.name.last}</h2>
                            <img src={user.picture.large} alt="" />
                            </div>;
                    }
                    
                    return(userElm)
                });

                this.setState({user: user, isLoading: false});
            });
        }
        catch(error) {
            this.setState({ error: error, isLoading: false });
        }
    }

    render() {
        let { user, isLoading, error } = this.state;

        if (error) {
            return <p>{error.message}</p>;
          }
          
        if (isLoading) {
            return <p>Loading...</p>;
          }

        return (
            <div>
                {user}
            </div>
        )
    }
}

export default Person;