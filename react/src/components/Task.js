import React, { Component } from 'react';

class Task extends Component {
  render() {
    const {
      title,
      description,
      estimated_time_in_minutes,
      due_date,
    } = this.props.task;

    return (
      <>
        <div className="top">
          <div className="category">
            <i className="material-icons">shopping_cart</i>
            Einkauf
          </div>
          <div className="distance">
            500 m
            <i className="material-icons">navigation</i>
          </div>
        </div>
        <div className="title">
          {title}
        </div>
        <div className="description">
          {description}
        </div>
        <div className="bottom">
          <div className="estimated_time">
            <i className="material-icons">timer</i>
            ca. {estimated_time_in_minutes} Minuten
          </div>
          <div className="duedate">
            bis zum {new Date(due_date).toLocaleDateString()}
            <i className="material-icons">date_range</i>
          </div>
        </div>
      </>
    );
  }
}

export default Task;
