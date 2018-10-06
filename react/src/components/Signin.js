import React, { Component } from 'react';
import { Field } from 'redux-form';

import Layout from './Layout';

export default class Signin extends Component {

  /* VALIDATION RULES */
  submit = values => this.props.signInAction(values);
  required = value => (!value ? 'wird benötigt' : undefined);
  minLength = min => value =>
    value && value.length < min ? `muss mindestens ${min} Zeichen enthalten` : undefined;
  minLength2 = this.minLength(2);

  renderField = ({ input, label, placeholder, type, meta: { touched, error, warning } }) => (
    <div className="field is-horizontal">
      <div className="field-label is-normal">
        <label htmlFor={input.name}>{label}</label>
      </div>
      <div className="field-body">
        <div className="field">
          <div className={`control ${input.name}`}>
            <input {...input} placeholder={placeholder} className="input" type={type} />
          </div>
          {touched && (error && <p className="help is-danger">{error}</p>)}
        </div>
      </div>
    </div>
  );

  // renderCheckbox = ({ input, meta: { touched, error } }) => (
  //   <div className="field is-horizontal">
  //     <div className="field-label" />
  //     <div className="field-body">
  //       <div className="field">
  //         <div className="control">
  //           <label className="checkbox">
  //             <input type="checkbox" {...input} />
  //             Hiermit bestätige ich, dass ich die{' '}
  //             <a href="/datenschutzhinweis" target="_blank">
  //               Datenschutzbestimmungen
  //             </a>{' '}
  //             akzeptiere.
  //           </label>
  //         </div>
  //         {touched && (error && <p className="help is-danger">{error}</p>)}
  //       </div>
  //     </div>
  //   </div>
  // );

  render() {
    const { authenticated, isInsideBusinessHours } = this.props;

    if (authenticated) return null;

    return (
      <Layout>
        <div className="text-wrap">
          <div className="text-sizer">
            {this.renderSigninForm()}
          </div>
        </div>
      </Layout>
    );
  }

  renderSigninForm() {
    const { handleSubmit } = this.props;

    return (
      <div className="guestsigninform">
        <form onSubmit={handleSubmit(this.submit)}>
          <Field
            name="username"
            label="Benutzername"
            component={this.renderField}
            type="text"
            placeholder="maxmustermann"
            validate={[this.required, this.minLength2]}
          />
          <Field
            name="password"
            label="Passwort"
            component={this.renderField}
            type="password"
            validate={[this.required, this.minLength2]}
          />
          {/*<Field*/}
            {/*name="accepted_tac"*/}
            {/*id="accepted_tac"*/}
            {/*component={this.renderCheckbox}*/}
            {/*type="checkbox"*/}
            {/*validate={[this.required]}*/}
          {/*/>*/}
          <div className="field is-horizontal">
            <div className="field-label" />
            <div className="field-body">
              <div className="field">
                <div className="control">
                  <button className="button is-primary" type="submit">
                    Login
                  </button>
                </div>
              </div>
            </div>
          </div>
        </form>
      </div>
    );
  }
}
