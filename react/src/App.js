import React, { Component } from 'react';
import './App.css';

// import ApiMock from './ApiMock';
// const {tasks} = ApiMock;

const renderTask = (task) => {
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
};

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isLoading: false,
      tasks: [],
      error: null,
    };
  }

  componentDidMount() {
    this.setState({ isLoading: true });

    fetch('https://api.taschengeldboerse.io')
      .then(response => response.json())
      .then(tasks => this.setState({ tasks, isLoading: false }))
      .catch(err => this.setState({ isLoading: false }));
  }

  render() {
    const { isLoading, tasks, error } = this.state;

    if(error !== null) {
      return (
        <div className="App">
          <header className="App-wrapper">
            <div>
              <h4>Beim Laden der Seite ist ein Fehler aufgetreten.</h4>
              <h4>Bitte versuchen Sie es in ein paar Minuten erneut.</h4>
            </div>
          </header>
        </div>
      )
    }

    return (
      <div className="App">
        <header className="App-wrapper">
          <h2>
            Taschengeldboerse
          </h2>

          { isLoading ? <div className="loading-spinner"></div> :
            <ul className="tasks">
              {tasks.length > 0 ? this.state.tasks.map(renderTask) : null}
            </ul> }

        </header>
      </div>
    );
  }
}

export default App;
