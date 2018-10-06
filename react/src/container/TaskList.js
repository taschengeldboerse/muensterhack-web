import React, { Component } from 'react';
import { connect } from 'react-redux';
import { fetchTasks } from '../store/actions/tasks';
import TaskList from '../components/TaskList'

class TaskListContainer extends Component {
  componentDidMount() {
    this.props.fetchTasks();
  }

  render() {
    const { isLoading, list, error } = this.props;

    if (isLoading) {
      return <div className="loading-spinner"></div>;
    }

    if(error) {
      return (
        <p>
          Beim Laden der Seite ist ein Fehler aufgetreten.
          <br />
          Bitte versuchen Sie es in ein paar Minuten erneut.
        </p>
      );
    }

    return <TaskList tasks={list} />;
  }
}

const mapStateToProps = state => (state.tasks);
const mapDispatchToProps = { fetchTasks };

export default connect(mapStateToProps, mapDispatchToProps)(TaskListContainer);
