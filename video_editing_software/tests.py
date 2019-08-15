# import json
# from django.test import TestCase
# from django.urls import reverse
#
# from loadbalance.models import LoadBalance, LoadBalanceRules
# from floating.models import Floating
# from network.models import Subnet
# from account.models import User
# from idc.models import CtUserPlatforms, SysPlatforms, SysPlatformDetails
#
# from mixer.backend.django import mixer
#
#
# class RuleViewApiTestCase(TestCase):
#     def setUp(self):
#         self.user = mixer.blend(User, ct_user_id='zhangkun', username='zhangkun')
#         self.dc = mixer.blend(SysPlatforms, uuid='cs_mock', type=1, service_url='http://127.0.0.1:8888/client/api/')
#         self.udc = mixer.blend(CtUserPlatforms, user_id=self.user.pk, tenant_uuid=json.dumps(dict(domain_id='/')),
#                                sysplatforms_id=self.dc.pk, dc=self.dc, keystone_user=self.user.username,
#                                tenant_name=json.dumps(dict(domain_name='/')),
#                                service_url='http://127.0.0.1:8888/client/api/')
#         self.dcd = mixer.blend(SysPlatformDetails, platform_id=self.dc.pk, name='apiKey')
#         self.dc1 = mixer.blend(SysPlatformDetails, platform_id=self.dc.pk, name='secret')
#         self.ip = mixer.blend(Floating, uuid='zhangkunuuid')
#         self.subnet = mixer.blend(Subnet, uuid='zhangkunuuid')
#         self.lb = mixer.blend(LoadBalance, ct_user_platforms_id=self.udc.pk, uuid='zhangkunuuid', ip_uuid=self.ip.uuid)
#
#     def test_loadbalance_rule_query(self):
#         url = reverse('lbr_query')
#
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 403)
#         data = {'ct_user_id': self.user.ct_user_id,
#                 'os_id': self.dc.uuid}
#
#         response = self.client.get(url, data)
#         self.assertEqual(response.status_code, 200)
#         res_data = response.json().get('results')
#         self.assertEqual(len(res_data), 0)
#
#     def test_loadbalance_rule_create(self):
#         url = reverse('lbr_query')
#
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 403)
#         data = {'ct_user_id': self.user.ct_user_id,
#                 'os_id': self.dc.uuid}
#
#         response = self.client.get(url, data)
#         self.assertEqual(response.status_code, 200)
#         res_data = response.json().get('results')
#         self.assertEqual(len(res_data), 0)
#
#         temp_data = dict(
#             algorithm='algorithm',
#             name='zhangkunlbr',
#             privateport=4353,
#             publicport=3424,
#             publicipid=self.ip.uuid,
#             lb_id=self.lb.uuid,
#             vmids='vmids',
#             Stickiness_method="Stickiness_method",
#             Health_Check="Health_Check",
#             subnetid=self.subnet.uuid,
#             description='description',
#             protocol='protocol',
#             pingpath="pingpath",
#             responsetimeout=10,
#             intervaltime="10",
#             healthythreshold=10,
#             unhealthythreshold=10,
#         )
#         temp_data.update(data)
#         url = reverse('lbr_create')
#         response = self.client.post(url, temp_data)
#         print(response.json())
#         self.assertEqual(response.status_code, 200)
#
#         url = reverse('lbr_query')
#         response = self.client.get(url, data)
#         self.assertEqual(response.status_code, 200)
#         res_data = response.json().get('results')
#         self.lb_rule_uuid = res_data[0].get('uuid')
#         print(f'self.lb_rule_uuid is : {self.lb_rule_uuid}')
#         self.assertEqual(len(res_data), 1)
#
#         url = reverse('lbr_delete')
#         temp_data = dict(id=self.lb_rule_uuid)
#         temp_data.update(data)
#         response = self.client.post(url, data=temp_data)
#         self.assertEqual(response.status_code, 200)
#         res_data = response.json().get('results')
#         print(f'res_data is : {res_data}')
#
#         url = reverse('lbr_query')
#         response = self.client.get(url, data)
#         self.assertEqual(response.status_code, 200)
#         res_data = response.json().get('results')
#         self.assertEqual(len(res_data), 0)
