import { reduxForm } from 'redux-form';
import { connect } from 'react-redux';
import { signInAction } from '../store/actions/auth';

import Signin from '../components/Signin';

const mapStateToProps = state => ({ authenticated: state.auth.authenticated });
const mapDispatchToProps = { signInAction };
const reduxFormSignin = reduxForm({ form: 'signin' })(Signin);

export default connect(mapStateToProps, mapDispatchToProps)(reduxFormSignin);
