"use client";

import React, { useState } from "react";
import { 
  LayoutDashboard, 
  UserCircle, 
  Link as LinkIcon, 
  Search, 
  AlertCircle, 
  Cpu, 
  ListChecks, 
  Settings,
  Share2
} from "lucide-react";
import { cn } from "@/lib/utils";

import DashboardOverview from "../components/dashboard/Overview";
import IdentityAnalyzer from "../components/dashboard/IdentityAnalyzer";
import SearchAnalyzer from "../components/dashboard/SearchAnalyzer";
import ProfileChecker from "../components/dashboard/ProfileChecker";
import IdentityGraph from "../components/dashboard/IdentityGraph";
import IssueList from "../components/dashboard/IssueList";
import AiAdvisor from "../components/dashboard/AiAdvisor";
import ActionPlan from "../components/dashboard/ActionPlan";

const NAV_ITEMS = [
  { id: "overview", label: "Overview", icon: LayoutDashboard },
  { id: "identity", label: "Identity", icon: UserCircle },
  { id: "profiles", label: "Profiles", icon: LinkIcon },
  { id: "search", label: "Search Queries", icon: Search },
  { id: "graph", label: "Identity Graph", icon: Share2 },
  { id: "issues", label: "Issues", icon: AlertCircle },
  { id: "ai-advisor", label: "AI Advisor", icon: Cpu },
  { id: "action-plan", label: "Action Plan", icon: ListChecks },
];

export default function Dashboard() {
  const [activeTab, setActiveTab] = useState("overview");

  const renderContent = () => {
    switch (activeTab) {
      case "overview": return <DashboardOverview />;
      case "identity": return <IdentityAnalyzer />;
      case "profiles": return <ProfileChecker />;
      case "search": return <SearchAnalyzer />;
      case "graph": return <IdentityGraph />;
      case "issues": return <IssueList />;
      case "ai-advisor": return <AiAdvisor />;
      case "action-plan": return <ActionPlan />;
      default: return <DashboardOverview />;
    }
  };

  return (
    <div className="flex h-screen w-full bg-background overflow-hidden text-foreground">
      {/* Sidebar */}
      <aside className="w-64 border-r border-border/50 bg-card/30 backdrop-blur-xl flex flex-col h-full shrink-0">
        <div className="p-6">
          <h1 className="text-xl font-bold gradient-text tracking-tight">Sanjay G L</h1>
          <p className="text-xs text-muted-foreground mt-1 uppercase tracking-wider">SEO Identity Analyzer</p>
        </div>
        
        <nav className="flex-1 px-4 space-y-1 overflow-y-auto">
          {NAV_ITEMS.map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => setActiveTab(item.id)}
                className={cn(
                  "w-full flex items-center space-x-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-all duration-200",
                  isActive 
                    ? "bg-primary/10 text-primary shadow-sm ring-1 ring-primary/20" 
                    : "text-muted-foreground hover:bg-muted hover:text-foreground"
                )}
              >
                <Icon className={cn("w-4 h-4", isActive ? "text-primary" : "text-muted-foreground")} />
                <span>{item.label}</span>
              </button>
            );
          })}
        </nav>

        <div className="p-4 border-t border-border/50">
          <button className="w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-sm font-medium text-muted-foreground hover:bg-muted transition-colors">
            <div className="flex items-center space-x-3">
              <Settings className="w-4 h-4" />
              <span>Settings</span>
            </div>
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 h-full overflow-y-auto bg-gradient-to-br from-background via-background to-secondary/10 relative">
        <div className="absolute top-0 right-0 p-4">
           <span className="inline-flex items-center rounded-full bg-primary/10 px-2.5 py-0.5 text-xs font-semibold text-primary border border-primary/20">
              Demo Analysis
           </span>
        </div>
        <div className="p-8 max-w-6xl mx-auto min-h-full">
          {renderContent()}
        </div>
      </main>
    </div>
  );
}
