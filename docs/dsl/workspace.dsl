workspace "Name" "Description" {

    !identifiers hierarchical

    model {
		user = person "User" "Klient sklepu firmy Qpik."
		supportAgentSystem = softwareSystem "System supportowy" "Zarządzania zapytaniami od klientami." {
			webAppContainer = container "Web Application" "Interfejs do komunikacji z agentem." "ASP .NET Core, Angular" "WebApp"
			agentContainer = container "Web API" "Logika agenta, komunikacja z OpenAI." "python, uvicorn" "WebAPI"
			dbContainer = container "Memory Database" "Zapisywanie sesji użytkownika z agentem." "Azure redis cache" "Database"
			statsContainer = container "Statistics Database" "Statystyki użycia agenta." "PostgreSQL" "Database"
			vectorContainer = container "Vector Database" "Zapisanie embeddingów dokumentów." "Chroma DB" "Database"
		}
		
		OpenAISystem = softwareSystem "OpenAI System" "LLM do komunikacji z użytkownikiem." "External, AI"
		qpikSystem = softwareSystem "Qpik System" "Obecna infrastruktura sklepu internetowego (w tym db z produktami i użytkownikami)." "External, Database"
		sendGridSystem = softwareSystem "SendGrid System" "API do wysyłania e-maili." "External, Mail"
		qpikFileServer = softwareSystem "Qpik File Server" "Server z plikami/dokumentacją firmy Qpik." "External, Folder"
		
		user -> supportAgentSystem.webAppContainer "Używa przez przeglądarkę"
		supportAgentSystem.webAppContainer -> supportAgentSystem.agentContainer "Wykonuje żądania HTTP" "HTTP"
		supportAgentSystem.agentContainer -> OpenAISystem "Wykonuje żądania HTTP" "HTTP"
		supportAgentSystem.agentContainer -> supportAgentSystem.vectorContainer "Zapis/odczyt wektorów dokumentów" "TCP"
		supportAgentSystem.agentContainer -> sendGridSystem "Wykonuje żądania HTTP" "HTTP"
		supportAgentSystem.agentContainer -> qpikFileServer "Wykonuje żądania HTTP" "HTTP"
		supportAgentSystem.agentContainer -> supportAgentSystem.dbContainer "Zapis/odczyt danych sesji" "TCP"
		supportAgentSystem.agentContainer -> qpikSystem "Zapis/odczyt danych z db" "TCP"
		supportAgentSystem.agentContainer -> supportAgentSystem.statsContainer "Zapis/odczyt danych z db" "TCP"
		
		live = deploymentEnvironment "Live" {
            deploymentNode "Azure Linux Server" {
                deploymentNode "Docker Container 1" {
                    webAppInstance = containerInstance supportAgentSystem.webAppContainer
                }
				
				deploymentNode "Docker Container 2" {
                    webApiInstance = containerInstance supportAgentSystem.agentContainer
                }
				
				deploymentNode "Docker Container 3" {
                    chromaInstance = containerInstance supportAgentSystem.vectorContainer
                }
				
				deploymentNode "Docker Container 4" {
                    chromaInstance = containerInstance supportAgentSystem.statsContainer
                }
            }
            
            deploymentNode "Azure Cloud" {
                deploymentNode "redis cache" {
                    databaseInstance = containerInstance supportAgentSystem.dbContainer
                }
            }
        }
    }

    views {
        systemContext supportAgentSystem "Context" {
            include *
        }
    
        container supportAgentSystem "Container" {
            include *
        }
        
        deployment supportAgentSystem "Live" "OnPremiseDeployment" {
            include *
            autolayout lr
        }
        
        styles {
            element "Element" {
                fontSize 30
            }
			
			relationship "Relationship" {
                color #000000
				fontSize 30
            }
        
            element "Software System" {
                background #1168bd
                color #ffffff
            }
            
            element "Container" {
                background #1168bd
                color #ffffff
            }
            
            element "Person" {
                shape person
                background #08427b
                color #ffffff
            }
            
            element "External" {
                background #999999
                color #ffffff
            }
			
			element "Folder" {
				shape Folder
			}
			
			element "Mail" {
				shape RoundedBox
			}
			
			element "AI" {
				shape Robot
			}
            
            element "Database" {
                shape Cylinder
            }
            
            element "WebApp" {
                shape WebBrowser
            }
        }
    }

    configuration {
        scope softwaresystem
    }

}