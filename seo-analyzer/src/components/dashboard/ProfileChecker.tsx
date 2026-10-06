"use client";

import React from "react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Globe, CheckCircle2, XCircle, ExternalLink, Code2, Users } from "lucide-react";

export default function ProfileChecker() {
  const profiles = [
    {
      platform: "Personal Website",
      icon: Globe,
      url: "https://sanjaygl30ai.vercel.app",
      color: "text-blue-400",
      checks: [
        { name: "Page title", status: "pass" },
        { name: "Meta description", status: "pass" },
        { name: "H1 structure", status: "pass" },
        { name: "Open Graph metadata", status: "warn" },
        { name: "Schema.org / Structured Data", status: "fail" },
        { name: "Internal links", status: "pass" },
      ]
    },
    {
      platform: "LinkedIn",
      icon: Users,
      url: "https://www.linkedin.com/in/sanjay-gl-b86631336",
      color: "text-blue-600",
      checks: [
        { name: "Profile URL format", status: "warn" },
        { name: "Name consistency", status: "pass" },
        { name: "Headline optimization", status: "pass" },
        { name: "About section", status: "warn" },
        { name: "Website link included", status: "pass" },
      ]
    },
    {
      platform: "GitHub",
      icon: Code2,
      url: "https://github.com/sanjayGL2006",
      color: "text-foreground",
      checks: [
        { name: "Username consistency", status: "warn" },
        { name: "Display name matches", status: "pass" },
        { name: "Bio includes keywords", status: "pass" },
        { name: "Website link included", status: "fail" },
        { name: "Profile README", status: "pass" },
      ]
    }
  ];

  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-700">
      <div>
        <h2 className="text-3xl font-bold tracking-tight">Profile Consistency Checker</h2>
        <p className="text-muted-foreground mt-1">Analyzing cross-platform SEO signals and missing links.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {profiles.map((profile) => {
          const Icon = profile.icon;
          const passed = profile.checks.filter(c => c.status === 'pass').length;
          const total = profile.checks.length;
          
          return (
            <Card key={profile.platform} className="flex flex-col">
              <CardHeader className="pb-4 border-b border-border/50">
                <div className="flex items-center justify-between mb-2">
                  <div className="flex items-center space-x-2">
                    <Icon className={`w-5 h-5 ${profile.color}`} />
                    <CardTitle className="text-lg">{profile.platform}</CardTitle>
                  </div>
                  <Badge variant={passed === total ? "success" : passed > total / 2 ? "warning" : "destructive"}>
                    {passed}/{total} Passed
                  </Badge>
                </div>
                <CardDescription className="flex items-center space-x-1 truncate hover:text-foreground transition-colors cursor-pointer group">
                  <span className="truncate">{profile.url}</span>
                  <ExternalLink className="w-3 h-3 opacity-0 group-hover:opacity-100 transition-opacity" />
                </CardDescription>
              </CardHeader>
              <CardContent className="pt-4 flex-1">
                <ul className="space-y-3">
                  {profile.checks.map((check, idx) => (
                    <li key={idx} className="flex items-center justify-between text-sm">
                      <span className="text-muted-foreground">{check.name}</span>
                      {check.status === "pass" ? (
                        <CheckCircle2 className="w-4 h-4 text-green-500" />
                      ) : check.status === "warn" ? (
                        <div className="w-4 h-4 rounded-full bg-yellow-500/20 flex items-center justify-center">
                          <div className="w-2 h-2 rounded-full bg-yellow-500" />
                        </div>
                      ) : (
                        <XCircle className="w-4 h-4 text-red-500" />
                      )}
                    </li>
                  ))}
                </ul>
              </CardContent>
            </Card>
          )
        })}
      </div>
    </div>
  );
}
