import React from 'react';
import Moment from 'moment';

import { List, PageHeader, Icon, Button, Descriptions } from 'antd';

Moment.locale('pt-BR');

const IconText = ({ type, text }) => (
    <span>
        <Icon type={type} style={{ marginRight: 8 }} />
        {text}
    </span>
);

const LaunchList = (props) => {
    return (
        <List
            itemLayout="vertical"
            size="large"
            pagination={{
                onChange: page => {
                    console.log(page);
                },
                pageSize: 6,
            }}
            dataSource={props.data}
            renderItem={item => (
                <List.Item>
                    <PageHeader
                        ghost={false}
                        title={item.rocket_name}
                        subTitle={item.customer}
                    >
                        <Descriptions size="small" column={3}>
                            <Descriptions.Item label="Nacionalidade">{item.nationality}</Descriptions.Item>
                            <Descriptions.Item label="Fabricante">
                                <a>{item.manufacturer}</a>
                            </Descriptions.Item>
                            <Descriptions.Item label="Data do Lançamento">{Moment(item.launch_date_utc).format('YYYY, DD MMM, HH:mm:, Z')}</Descriptions.Item>
                            <Descriptions.Item label="Tipo do Foguete">{item.rocket_type}</Descriptions.Item>
                            <Descriptions.Item label="Local do Lançamento">
                                {item.site_name}
                            </Descriptions.Item>
                        </Descriptions>
                    </PageHeader>
                </List.Item>
            )}
        />
    );
}

export default LaunchList;