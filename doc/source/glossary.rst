..
    Copyright 2012 Endre Karlson for Bouvet ASA

    Licensed under the Apache License, Version 2.0 (the "License"); you may
    not use this file except in compliance with the License. You may obtain
    a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
    License for the specific language governing permissions and limitations
    under the License.

.. _architecture:


============
Glossary
============

.. glossary::
   agent
     Software service running on nodes that executes actions towards typically
     nameservers like BIND or similar.
   central
     Software service running on a central management node that stores
     information persistantly in a backend storage using a configurable driver
     like SQLAlchemy or other.
   api
     HTTP REST API service for Designate
   mq
     A message queue, typically something like RabbitMQ or ZeroMQ
   storage
     A backend for storing data/information persistantly. Typically MongoDB or
     a SQL based server software.
