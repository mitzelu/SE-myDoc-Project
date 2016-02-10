
Project on Software Engineering Course, CVUT 

##Specifications: 

- You work in teams of 3-5 people. The supervisor makes the final decision about the team structure.
- Work within the term is divided into 3 iterations.
- At the end of each iteration, the team presents the results and submit the required documentation.
- The project must solve a non-trivial business problem and plan to develop a complex information system.
- The system must be designed using object-oriented approach and at least 2-layered architecture.


##Content of the iterations

- [**1st iteration**](https://github.com/mitzelu/SE-myDoc-Project/blob/master/documentation-EA-diagrams/MyDoc-analysis.pdf)
	- mainly analysis and inception of design
	- analysis of business processes (most important business-oriented processes in the domain that should be supported and improved by the system)
	- UML Activity diagrams + textual description of the processes
	- requirements analysis
	- requirements catalogue - a list of functional and non-functional requirements with descriptions
	- use case model (List of actors and their description, UML Use Case diagrams - actors, use cases, boundary, Scenarios - main scenario, alternative scenarios, Mapping of the use cases onto the requirements)
	- domain model
	- UML Class diagram(s) - classes with attributes, associations with names and cardinalities
	- UML State diagram(s) for specific entities with important states

- [**2nd iteration**](https://github.com/mitzelu/SE-myDoc-Project/blob/master/documentation-EA-diagrams/MyDoc-design_v2.pdf)
	- mainly design, finishing analysis, inception of implementation
	- finalization of the analysis based on design decisions
	- design decisions, specification of architecture and technologies
	- description of chosen technologies and frameworks
		- User interface
		- Data persistence
		- Business logic, Dependency Injection, etc.
	- software architecture
		- UML Component diagram - components, dependencies, interfaces
		- description of basic system components / layers, principle of their isolation (interfaces) - not necessary to define exact interfaces
	- design model
		- UML Class diagrams - classes, attributes, methods, directed associations, role names, cardinalities
		- description of the classes
		- based on chosen architecture, technologies and domain model
		- focused on realization of the crucial use cases - definition of classes required to realize them
		- logically organized in packages according to the chosen architecture
	- Contents
		- Data objects - classes to hold the data, inspired by the domain model, extended with the data types, associations' orientation, role names
		- Implementation classes - classes providing the behaviour - data persistence, business logic, validations, etc.
		- UI classes - classes of the user interface, providing the data to user and collecting the input
		- Assignment of responsibilities - added methods of the business logic and other processes to adequate classes
	- realization of Use Cases
		- UML Sequence diagrams or UML Communication diagrams + Descriptions
		- realization of the crucial use cases by the system classes
		- communication of the instances of the classes from the design model
	- database model
		- UML Class diagram
		- structure of the system database
		- description of database tables, primary and foreign keys, data types, realization of many-to-many relations

- **3rd iteration**
	- mainly implementation, finishing analysis and design
		- implementation of the application prototype
			- the implementation must comply to the design documentation - in structure, in names, in communication principles, etc.
			- in case the implementation differs on purpose, the design documentation should be updated!
	- prototype implementation
		- implementation of the most crucial use cases
		- the UI is not important, not all situations need to be checked, etc. - it is a prototype
		- the prototype is presented in the class
	- documentation
		- [Installation guide](https://github.com/mitzelu/SE-myDoc-Project/blob/master/documentation-EA-diagrams/installation_guide.pdf)
			- UML Deployment diagram + description
				- Description of the structure of the environment and requirements - OS, Java, browser, etc.
			- Description the process of installation and start of the application
		- [Implementation documentation](https://github.com/mitzelu/SE-myDoc-Project/blob/master/documentation-EA-diagrams/code-doc.pdf)
			- Documentation automatically generated from the source code - JavaDoc, PHPDoc, etc.
			- Detailed documentation of interfaces and classes (with methods) implementing the implemented use cases
		- Source code
			- Complete source code of the application