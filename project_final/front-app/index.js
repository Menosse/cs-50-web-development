import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';



ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

//import reportWebVitals from './reportWebVitals';

/*
import React from 'react';
import ReactDOM from 'react-dom';
import './Index.css';
*/


/*
export default class FetchProject extends React.Component {

  state= {
    loading: true,
    project: null
  }

  async componentDidMount(){
    const base_url = "http://localhost:8000"
    const endpoint = '/project/4'
    const url = base_url+endpoint
    //console.log("url: " + url);
    //console.log('test 1')
    const response = await fetch(url);
    //console.log(response)
    const data = await response.json();
    this.setState({project: data, loading: false});
    //console.log(data);
  }

  render(){
    return <div>
      {this.state.loading || !this.state.project ? (
        <div>loading!!!</div>
        ) : (
         <div>
          <div>project!?!</div>
          <div>{this.state.project.id}</div>
          <div>{this.state.project.name}</div>
          <div>{this.state.project.description}</div>
          <img src={this.state.project.main_image} alt='nothing' />
         </div>
        )}
    </div>
  }


}

ReactDOM.render(
  <FetchProject />,
  document.getElementById('root')
);
*/