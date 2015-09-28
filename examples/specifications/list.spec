{
  "apis": {
    "children": {
        "/lists/{id}/tasks": {
          "RESTName": "task",
          "resourceName": "tasks",
          "entityName": "Task",
          "operations": [
              { "availability": null, "method": "GET" },
              { "availability": null, "method": "POST" }
          ]
        }
    },
    "parents": {
        "/lists": {
            "RESTName": "list",
            "resourceName": "lists",
            "operations": [
            {"availability": null, "method": "GET" },
            {"availability": null, "method": "POST"}
            ]
        }
    },
    "self": {
      "/lists/{id}": {
        "RESTName": "list",
        "resourceName": "lists",
        "entityName": "List",
        "operations": [
            { "availability": null, "method": "PUT" },
            { "availability": null, "method": "DELETE" },
            { "availability": null, "method": "GET" }
        ]
      }
    }
  },
  "model": {
    "RESTName": "list",
    "description": "Represent a a list of task to do",
    "entityName": "List",
    "package": "todo-list",
    "resourceName": "lists",
    "attributes": {
      "title": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "The title of the task",
        "exposed": true,
        "filterable": true,
        "format": null,
        "maxLength": 1024,
        "maxValue": null,
        "minLength": 1,
        "minValue": null,
        "orderable": true,
        "readOnly": false,
        "required": true,
        "transient": false,
        "type": "string",
        "unique": true
      },
      "description": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "The description of the list",
        "exposed": true,
        "filterable": true,
        "format": null,
        "maxLength": 2048,
        "maxValue": null,
        "minLength": 1,
        "minValue": null,
        "orderable": true,
        "readOnly": false,
        "required": false,
        "transient": false,
        "type": "string",
        "unique": true
      }
    }
  }
}