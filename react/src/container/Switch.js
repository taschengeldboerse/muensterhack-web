import React, { Component } from 'react';
import { connect } from 'react-redux';

import TaskList from './TaskList';
import TaskCreateButton from './TaskCreateButton';
import TaskCreateForm from './TaskCreateForm';

class Switch extends Component {
  render() {
    const { view } = this.props;

    if (view === 'form') {
      return <TaskCreateForm />;
    }

    return (
      <>
        <TaskList />
        <TaskCreateButton />
      </>
    );
  }
}

const mapStateToProps = state => ({ view: state.view });

export default connect(mapStateToProps)(Switch);
