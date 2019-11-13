import React from 'react';
import axios from 'axios';
import Launch from '../components/Launch'

class NextLaunch extends React.Component {
    state = {
        nextLaunch: {}
    }
    
    componentDidMount() {
        axios.get('http://0.0.0.0:8000/api/next/')
            .then(res => {
                console.log(res.data);
                this.setState({
                    nextLaunch: res.data
                })
            })
    }

    render() {
        return (
            <Launch data={this.state.nextLaunch} />
        );
    }
}
export default NextLaunch;