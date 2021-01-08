import React, {Component} from 'react';
import './Projects.css'
 
class Projects extends Component {
  constructor() {
    super();
    this.state = {
        //project: [],
        //project: {id, name, description, main_image},
        project: {},
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
      await fetch('http://localhost:8000/project/5')
      //await fetch('http://localhost:8000/list_projects')
      .then(results => {
        //console.log(results)
          return results.json();
      })
      .then(data => {
        //console.log('data',data)
        //this.setState({project: {id:data.id, name:data.name, description:data.description, main_image:data.main_image}, isLoading: false});
        this.setState({project: data, isLoading: false})

      });
  }
  catch(error) {
      this.setState({ error: error, isLoading: false });
  }
}

render() {
  let { project, isLoading, error } = this.state;
  //console.log('render',project)

  if (error) {
      return <p>{error.message}</p>;
    }
    
  if (isLoading) {
      return <p>Loading...</p>;
    }

  return (
      <div className='project-container'>
        <div className='project-wrapper'>
          <div className={'project ' + project.id} id={project.id}>
            <h1>{project.name}</h1>
            <h3>{project.description}</h3>
            <img src={project.main_image} alt='Loading...' />
          </div>
        </div>
      </div>
  )
}
}

 
export default Projects;