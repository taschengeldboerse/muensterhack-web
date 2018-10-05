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
            Taschengeldboerse
          </h2>

          <ul className="tasks">
            {tasks.map(task => {
              return (
                <li className="task">
                  <div className="top">
                    <div className="category">
                      <i class="material-icons">shopping_cart</i>
                      Einkauf
                    </div>
                    <div className="distance">
                      500 m
                      <i class="material-icons">navigation</i>
                    </div>
                  </div>
                  <div className="title">
                    {task.title}
                  </div>
                  <div className="description">
                    {task.description}
                  </div>
                  <div className="bottom">
                    <div className="estimated_time">
                      <i class="material-icons">timer</i>
                      ca. {task.estimated_time_in_minutes} Minuten
                    </div>
                    <div className="duedate">
                      bis zum {new Date(task.duedate).toLocaleDateString()}
                      <i class="material-icons">date_range</i>
                    </div>
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
