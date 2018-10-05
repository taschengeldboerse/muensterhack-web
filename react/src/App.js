import React, { Component } from 'react';
import './App.css';
import ApiMock from './ApiMock';

const {tasks} = ApiMock;

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-wrapper">
          <h2>
            <i class="material-icons">monetization_on</i>
            Taschengeldboerse
          </h2>

          <ul className="tasks">
            {tasks.map(task => {
              return (
                <li className="task">
                  <div className="category">Einkauf</div>
                  <div className="distance">
                    500 m
                    <i class="material-icons">navigation</i>
                  </div>
                  <div className="title">
                    {task.title}
                  </div>
                  <div className="description">
                    {task.description}
                  </div>
                  <div className="estimated_time">
                    {task.estimated_time_in_minutes}
                    <i class="material-icons">timer</i>
                  </div>
                  <div className="duedate">
                    {new Date(task.duedate).toLocaleDateString()}
                    <i class="material-icons">date_range</i>
                  </div>
                </li>
              )
            })}
          </ul>
        </header>
      </div>
    );
  }
}

export default App;
