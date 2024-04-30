import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  state = {
    details: []
  };

  componentDidMount() {
    axios.get('http://localhost:8000/')
      .then(res => {
        if (res.data && Array.isArray(res.data)) { // Check if response data is not empty
          this.setState({
            details: res.data
          });
        } else {
          console.error('Invalid response data:', res.data);
        }
      })
      .catch(err => {
        console.error("Error fetching data:", err);
      });
  }

  render() {
    return (
      <div>
        <h1>Data From Django Server</h1>
        
        {this.state.details.map((output, id) => (
          <div key={id}>
            <h2>{output.food}</h2>
            <h3>{output.ingredient}</h3>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
