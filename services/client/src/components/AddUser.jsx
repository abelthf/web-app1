import React from 'react';

const AddUser = (props) => {
  return (
    <form onSubmit={(event) => event.preventDefault()}>
      <div className="field">
        <input
          name="username"
          className="input is-large"
          type="text"
          placeholder="Enter a username"
          required
          value={props.username}  // new
          onChange={props.handleChange}  // new

        />
      </div>
      <div className="field">
        <input
          name="email"
          className="input is-large"
          type="email"
          placeholder="Enter an email address"
          required
          value={props.email}  // new
          onChange={props.handleChange}  // new

        />
      </div>
      <input
        type="submit"
        className="button is-primary is-large is-fullwidth"
        value="Submit"
      />
    </form>
  )
};

export default AddUser;
