import React from 'react';
import axios from 'axios';
import LaunchList from '../components/LaunchList'

class PastLaunchList extends React.Component {
    state = {
        pastLaunches: []
    }
    
    componentDidMount() {
        axios.get('http://0.0.0.0:8000/api/past/')
            .then(res => {
                console.log(res.data);
                this.setState({
                    pastLaunches: res.data
                })
            })
    }

    render() {
        return (
            <LaunchList data={this.state.pastLaunches} />
        );
    }
}
export default PastLaunchList;