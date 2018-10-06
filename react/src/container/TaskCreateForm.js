import { reduxForm } from 'redux-form';
import { connect } from 'react-redux';
import { submitTask } from '../store/actions/tasks';

import TaskCreateForm from '../components/TaskCreateForm';

const mapStateToProps = state => ({});
const mapDispatchToProps = { submitTask };
const reduxFormTaskCreate = reduxForm({ form: 'task_create' })(TaskCreateForm);

export default connect(mapStateToProps, mapDispatchToProps)(reduxFormTaskCreate);
