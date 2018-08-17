import React from 'react';
import { Modal, Button } from 'antd';
import axios from 'axios';
import decode from 'jwt-decode';

import SignInForm from './SignInForm'


function SignOut(props) {
  return (
    <Button 
      type="primary"
      onClick={props.handleSignOut}>
      Sign Out
    </Button>
  );
}

class SignIn extends React.Component {
  constructor(props) {
    super(props);
    this.handleSignIn = this.handleSignIn.bind(this);
    this.handleSignOut = this.handleSignOut.bind(this);
    this.state = {
      isSignedIn: false
    };
  }

  componentDidMount() {
    // Check if token exists and isn't expired
    const token = localStorage.getItem('id_token');
    if (token) {
      const decoded = decode(token);
      const current_time = new Date().getTime() / 1000;
      if (decoded.exp && decoded.exp < current_time) {
	/* Token is expired, sign out */
	this.handleSignOut();
      } else {
	this.signInWithToken(token);
      }
    }
    const user = localStorage.getItem('user');
    if (user) {
      this.props.handleAuthChange(JSON.parse(user));
    }
  }

  signInWithToken(token) {
    localStorage.setItem('id_token', token);
    axios.defaults.headers.common['Authorization'] = "Bearer " + token;
    axios.defaults.xsrfCookieName = "csrftoken";
    axios.defaults.xsrfHeaderName = "X-CSRFToken";
    this.setState({isSignedIn: true});
  }

  handleSignIn(username, password) {
    console.log("Trying to sign in " + username);
    axios.post('/api/auth/', {
      username: username,
      password: password
    })
    .then((response) => {
      const token = response.data.token;
      const user = response.data.user;
      console.log(response.headers);
      if (token) {
	console.log("Signed in " + username);
	this.signInWithToken(token);
	if (user) {
	  localStorage.setItem('user', JSON.stringify(user));
	  this.props.handleAuthChange(user);
	}
      } else {
	console.log("Failed to sign in " + username);
	Modal.error({
	  title: "Unable to sign in",
	  content: "Please check username and password and try again",
	  maskClosable: true,
	})
      }
    })
    .catch((error) => {
      console.log(error);
      Modal.error({
	title: "Unable to sign in",
	content: "Please check username and password and try again",
	maskClosable: true,
      })
    });
  }

  handleSignOut() {
    localStorage.removeItem("id_token");
    localStorage.removeItem("user");
    this.props.handleAuthChange(null);
    delete axios.defaults.headers.common["Authorization"];

    console.log("Signed out");
    this.setState({isSignedIn: false});
  }

  render() {
    const signInOrOut = this.state.isSignedIn ? (
      <SignOut handleSignOut={this.handleSignOut} />
    ) : (
      <SignInForm handleSignIn={this.handleSignIn} />
    );

    return (
      <div className="SignIn">
        {signInOrOut}
      </div>
    );
  }
}

export default SignIn
