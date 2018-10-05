import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import ApiMock from './ApiMock';

const {tasks} = ApiMock;

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <i class="material-icons">face</i>
          <p>{JSON.stringify(tasks)}</p>
        </header>
      </div>
    );
  }
}

export default App;
