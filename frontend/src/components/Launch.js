import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getLaunch, deleteLead } from "../../actions/launches";

export class Launch extends Component {
  static propTypes = {
    launches: PropTypes.array.isRequired,
    getLaunch: PropTypes.func.isRequired,
    deleteLead: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getLaunch();
  }

  render() {
    return (
      <Fragment>
        <h2>Launch</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Email</th>
              <th>Message</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {this.props.launches.map(lead => (
              <tr key={lead.id}>
                <td>{lead.id}</td>
                <td>{lead.name}</td>
                <td>{lead.email}</td>
                <td>{lead.message}</td>
                <td>
                  <button
                    onClick={this.props.deleteLead.bind(this, lead.id)}
                    className="btn btn-danger btn-sm"
                  >
                    {" "}
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  launches: state.launches.launches
});

export default connect(
  mapStateToProps,
  { getLaunch, deleteLead }
)(Launch);