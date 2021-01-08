import React, {Component} from 'react';
import './ListProjects.css'
 
class ListProjects extends Component {
  constructor() {
    super();
    this.state = {
        //project: [],
        //project: {id, name, description, main_image},
        list_project: {},
        isLoading: false,
        error: null
    }
}

componentDidMount() {
  this.setState({ isLoading: true });
  this.fetchProject();
}

fetchProject = async() => {
  try {
      await fetch('http://localhost:8000/list_projects')
      .then(results => {
        //console.log(results)
          return results.json();
      })
      .then(data => {
        //console.log('data',data)
        //this.setState({project: {id:data.id, name:data.name, description:data.description, main_image:data.main_image}, isLoading: false});
        this.setState({list_project: data.projects, isLoading: false})

      });
  }
  catch(error) {
      this.setState({ error: error, isLoading: false });
  }
}

render() {
  let { list_project, isLoading, error } = this.state;

  if (error) {
      return <p>{error.message}</p>;
    }
    
  if (isLoading) {
      return <p>Loading...</p>;
  }
  return (
      <div className='list_project-container'>
        <div className='list_project-wrapper'>
          <div className={'list_project ' + list_project.id} id={list_project.id}>
            <h1>{list_project.name}</h1>
            <h3>{list_project.description}</h3>
            <img src={list_project.main_image} alt='Loading...' />
          </div>
        </div>
      </div>
  )
}
}

 
export default ListProjects;