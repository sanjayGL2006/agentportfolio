"use client";

import React from "react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Search, Sparkles } from "lucide-react";

export default function SearchAnalyzer() {
  const queries = [
    { query: '"Sanjay G L"', relevance: "High", match: "Strong", profile: "LinkedIn, Website", rec: "Maintain exact match in titles" },
    { query: '"Sanjay GL"', relevance: "Medium", match: "Partial", profile: "GitHub", rec: "Redirect/Alias to primary name" },
    { query: '"Sanjaygl"', relevance: "Low", match: "Weak", profile: "None", rec: "Not priority, but monitor" },
    { query: '"Sanjaygl2006"', relevance: "Medium", match: "Username", profile: "GitHub", rec: "Unify username if possible" },
    { query: '"Sanjaygl30ai"', relevance: "High", match: "Brand", profile: "Website", rec: "Use as primary universal handle" },
    { query: '"Sanjay G L" AI', relevance: "High", match: "Intent", profile: "Website", rec: "Add AI keywords to LinkedIn headline" },
    { query: '"Sanjay G L" developer', relevance: "High", match: "Intent", profile: "Website, GitHub", rec: "Optimize Website meta description" },
  ];

  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-700">
      <div>
        <h2 className="text-3xl font-bold tracking-tight">How Search Engines See Me</h2>
        <p className="text-muted-foreground mt-1">Estimated search visibility for different queries.</p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <Sparkles className="w-5 h-5 text-primary" />
            <span>Search Query Analysis</span>
          </CardTitle>
          <CardDescription>
            This is an estimated analysis based on your provided identities and SEO best practices.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="overflow-x-auto">
            <table className="w-full text-sm text-left">
              <thead className="text-xs text-muted-foreground uppercase bg-muted/50 rounded-t-lg">
                <tr>
                  <th className="px-4 py-3 rounded-tl-lg">Search Query</th>
                  <th className="px-4 py-3">Relevance</th>
                  <th className="px-4 py-3">Identity Match</th>
                  <th className="px-4 py-3">Primary Profiles</th>
                  <th className="px-4 py-3 rounded-tr-lg">SEO Recommendation</th>
                </tr>
              </thead>
              <tbody>
                {queries.map((q, idx) => (
                  <tr key={idx} className="border-b border-border/50 hover:bg-muted/30 transition-colors">
                    <td className="px-4 py-4 font-medium flex items-center space-x-2">
                      <Search className="w-3 h-3 text-muted-foreground" />
                      <span>{q.query}</span>
                    </td>
                    <td className="px-4 py-4">
                      <Badge variant={q.relevance === "High" ? "success" : q.relevance === "Medium" ? "warning" : "secondary"}>
                        {q.relevance}
                      </Badge>
                    </td>
                    <td className="px-4 py-4 text-foreground">{q.match}</td>
                    <td className="px-4 py-4 text-muted-foreground">{q.profile}</td>
                    <td className="px-4 py-4 text-primary font-medium">{q.rec}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
