import React from 'react';
import UpcomingLaunchList from './UpcomingLaunchListView';

import { Layout, Menu, Icon, Tabs } from 'antd';
const TabPane = Tabs.TabPane;
const { Content, Footer } = Layout;

class CustomLayout extends React.Component {
    state = {
        current: 'mail',
    };

    handleClick = e => {
        console.log('click ', e);
        this.setState({
            current: e.key,
        });
    };

    callback(key) {
        console.log(key);
    }
      

    render() {
        return (
            <Layout>
                <Content style={{ background: '#fff', padding: '0 20px' }}>
                <Tabs defaultActiveKey="1" onChange={this.callback}>
                    <TabPane tab="Próximo Lançamento" key="1">

                    </TabPane>
                    <TabPane tab="Último Lançamento" key="2">

                    </TabPane>
                    <TabPane tab="Próximos Lançamentos" key="3">
                        <UpcomingLaunchList />
                    </TabPane>
                    <TabPane tab="Lançamentos Passados" key="4">
                    </TabPane>
                </Tabs>
                    <div style={{ background: '#fff', padding: 24, minHeight: 280 }}>
                    </div>
                </Content>
                <Footer style={{ textAlign: 'center', bottom: 0 }}></Footer>
            </Layout>
        );
    }
}

export default CustomLayout;