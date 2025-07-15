import React from 'react';
import { ArrowRight, Play, CheckCircle, Star, Shield, FileText, BarChart3, MessageCircle, Sparkles, Zap } from 'lucide-react';

const LandingPage = () => {
  return (
    <div className="min-h-screen bg-gray-50 text-gray-900 overflow-x-hidden">
      {/* Background Gradient */}
      <div className="fixed inset-0 bg-gradient-to-br from-blue-50 via-white to-purple-50"></div>
      <div className="fixed inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-purple-100/30 via-transparent to-blue-100/20"></div>

      {/* Navigation */}
      <nav className="relative z-50 fixed top-0 w-full bg-white/90 backdrop-blur-xl border-b border-gray-200/50 shadow-sm">
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className="w-8 h-8 bg-gradient-to-r from-purple-500 to-blue-500 rounded-lg flex items-center justify-center">
                <Sparkles className="w-5 h-5 text-white" />
              </div>
              <span className="text-xl font-bold bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">
                ConforMind
              </span>
            </div>
            <div className="hidden md:flex items-center gap-8">
              <a href="#features" className="text-gray-600 hover:text-gray-900 transition-colors">Fonctionnalités</a>
              <a href="#about" className="text-gray-600 hover:text-gray-900 transition-colors">À propos</a>
              <a href="#contact" className="text-gray-600 hover:text-gray-900 transition-colors">Contact</a>
              <button className="bg-gradient-to-r from-purple-500 to-blue-500 text-white px-6 py-2 rounded-lg font-medium hover:opacity-90 transition-opacity shadow-lg">
                Démo gratuite
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="relative pt-32 pb-20 px-6">
        <div className="max-w-7xl mx-auto">
          <div className="text-center max-w-5xl mx-auto">
            {/* Floating Badge */}
            <div className="inline-flex items-center gap-2 bg-purple-50 border border-purple-200 text-purple-700 px-4 py-2 rounded-full text-sm font-medium mb-8 backdrop-blur-sm shadow-sm">
              <div className="w-2 h-2 bg-purple-500 rounded-full animate-pulse"></div>
              EU AI Act : Obligations renforcées en 2025
            </div>

            {/* Main Headline */}
            <h1 className="text-6xl md:text-7xl lg:text-8xl font-bold mb-8 leading-[0.9] tracking-tight">
              <span className="bg-gradient-to-r from-gray-900 via-gray-700 to-gray-800 bg-clip-text text-transparent">
                Conformité
              </span>
              <br />
              <span className="bg-gradient-to-r from-purple-600 via-blue-600 to-indigo-600 bg-clip-text text-transparent">
                EU AI Act
              </span>
              <br />
              <span className="text-gray-500">Automatisée</span>
            </h1>

            {/* Subtitle */}
            <p className="text-xl md:text-2xl text-gray-600 mb-12 max-w-3xl mx-auto leading-relaxed">
              Transformez vos obligations réglementaires en avantage concurrentiel. 
              <span className="text-purple-600 font-medium">Analyse automatisée</span>, 
              <span className="text-blue-600 font-medium"> documentation complète</span>, 
              <span className="text-indigo-600 font-medium"> conformité garantie</span>.
            </p>

            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-16">
              <button className="bg-gradient-to-r from-purple-500 to-blue-500 text-white px-8 py-4 rounded-xl text-lg font-medium hover:shadow-2xl hover:shadow-purple-500/25 transition-all duration-300 flex items-center gap-2 group">
                <Zap className="w-5 h-5" />
                Analyser votre IA
                <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
              </button>
              <button className="flex items-center gap-3 text-gray-600 hover:text-gray-900 transition-colors group">
                <div className="w-12 h-12 bg-white border border-gray-200 rounded-full flex items-center justify-center group-hover:border-purple-300 transition-colors shadow-sm">
                  <Play className="w-5 h-5 ml-0.5" />
                </div>
                <span>Voir la démo</span>
              </button>
            </div>

            {/* Trust Indicators */}
            <div className="flex flex-wrap justify-center gap-8 text-sm text-gray-500">
              <div className="flex items-center gap-2">
                <CheckCircle className="w-4 h-4 text-green-500" />
                <span>Validation juridique européenne</span>
              </div>
              <div className="flex items-center gap-2">
                <Shield className="w-4 h-4 text-blue-500" />
                <span>Hébergement sécurisé EU</span>
              </div>
              <div className="flex items-center gap-2">
                <Star className="w-4 h-4 text-yellow-500" />
                <span>Certifié par des experts</span>
              </div>
            </div>
          </div>
        </div>

        {/* Floating Elements */}
        <div className="absolute top-40 left-10 w-20 h-20 bg-gradient-to-r from-purple-200/30 to-blue-200/30 rounded-full blur-xl"></div>
        <div className="absolute bottom-40 right-16 w-32 h-32 bg-gradient-to-r from-blue-200/30 to-indigo-200/30 rounded-full blur-xl"></div>
      </section>

      {/* Problem/Solution */}
      <section className="relative py-20 px-6">
        <div className="max-w-7xl mx-auto">
          <div className="grid lg:grid-cols-2 gap-20 items-center">
            {/* Problem */}
            <div className="space-y-8">
              <div>
                <div className="text-red-500 text-sm font-semibold uppercase tracking-wider mb-4">Le défi</div>
                <h2 className="text-4xl md:text-5xl font-bold mb-6 leading-tight text-gray-900">
                  L'EU AI Act redéfinit
                  <br />
                  <span className="text-gray-500">les règles du jeu</span>
                </h2>
              </div>
              
              <div className="space-y-6">
                <div className="flex gap-4 p-4 bg-white/60 border border-gray-200 rounded-xl backdrop-blur-sm shadow-sm">
                  <div className="w-2 h-2 bg-red-400 rounded-full mt-2"></div>
                  <span className="text-gray-700">Classification obligatoire de tous vos systèmes IA selon leur niveau de risque</span>
                </div>
                <div className="flex gap-4 p-4 bg-white/60 border border-gray-200 rounded-xl backdrop-blur-sm shadow-sm">
                  <div className="w-2 h-2 bg-red-400 rounded-full mt-2"></div>
                  <span className="text-gray-700">Documentation technique exhaustive et traçabilité complète</span>
                </div>
                <div className="flex gap-4 p-4 bg-white/60 border border-gray-200 rounded-xl backdrop-blur-sm shadow-sm">
                  <div className="w-2 h-2 bg-red-400 rounded-full mt-2"></div>
                  <span className="text-gray-700">Évaluation continue des biais et mesures correctives</span>
                </div>
                <div className="flex gap-4 p-4 bg-white/60 border border-gray-200 rounded-xl backdrop-blur-sm shadow-sm">
                  <div className="w-2 h-2 bg-red-400 rounded-full mt-2"></div>
                  <span className="text-gray-700">Complexité juridique nécessitant une expertise spécialisée</span>
                </div>
              </div>
            </div>

            {/* Solution */}
            <div className="space-y-8">
              <div>
                <div className="text-purple-600 text-sm font-semibold uppercase tracking-wider mb-4">Notre solution</div>
                <h2 className="text-4xl md:text-5xl font-bold mb-6 leading-tight text-gray-900">
                  <span className="bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">
                    Intelligence artificielle
                  </span>
                  <br />
                  <span className="text-gray-500">pour l'IA</span>
                </h2>
              </div>

              <div className="space-y-6">
                <div className="flex gap-4 p-4 bg-gradient-to-r from-purple-50 to-blue-50 border border-purple-200 rounded-xl backdrop-blur-sm shadow-sm">
                  <CheckCircle className="w-6 h-6 text-green-500 mt-0.5" />
                  <span className="text-gray-700">Classification automatique et instantanée selon l'EU AI Act</span>
                </div>
                <div className="flex gap-4 p-4 bg-gradient-to-r from-purple-50 to-blue-50 border border-purple-200 rounded-xl backdrop-blur-sm shadow-sm">
                  <CheckCircle className="w-6 h-6 text-green-500 mt-0.5" />
                  <span className="text-gray-700">Génération intelligente de toute la documentation requise</span>
                </div>
                <div className="flex gap-4 p-4 bg-gradient-to-r from-purple-50 to-blue-50 border border-purple-200 rounded-xl backdrop-blur-sm shadow-sm">
                  <CheckCircle className="w-6 h-6 text-green-500 mt-0.5" />
                  <span className="text-gray-700">Détection automatique des biais avec recommandations</span>
                </div>
                <div className="flex gap-4 p-4 bg-gradient-to-r from-purple-50 to-blue-50 border border-purple-200 rounded-xl backdrop-blur-sm shadow-sm">
                  <CheckCircle className="w-6 h-6 text-green-500 mt-0.5" />
                  <span className="text-gray-700">Validation par nos experts juridiques européens</span>
                </div>
              </div>

              {/* Metrics */}
              <div className="grid grid-cols-3 gap-6 pt-8">
                <div className="text-center p-4 bg-white/60 border border-gray-200 rounded-xl shadow-sm">
                  <div className="text-2xl font-bold bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">Semaines</div>
                  <div className="text-xs text-gray-500">vs mois manuels</div>
                </div>
                <div className="text-center p-4 bg-white/60 border border-gray-200 rounded-xl shadow-sm">
                  <div className="text-2xl font-bold bg-gradient-to-r from-green-600 to-emerald-600 bg-clip-text text-transparent">95%</div>
                  <div className="text-xs text-gray-500">Précision garantie</div>
                </div>
                <div className="text-center p-4 bg-white/60 border border-gray-200 rounded-xl shadow-sm">
                  <div className="text-2xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">24/7</div>
                  <div className="text-xs text-gray-500">Support expert</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="relative py-20 px-6">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold mb-6 text-gray-900">
              Plateforme complète
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Tous les outils nécessaires pour une conformité EU AI Act sans effort
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {/* Feature 1 */}
            <div className="group p-8 bg-white/70 border border-gray-200 rounded-2xl hover:border-purple-300 transition-all duration-300 backdrop-blur-sm shadow-lg hover:shadow-xl">
              <div className="w-12 h-12 bg-gradient-to-r from-purple-500 to-blue-500 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform shadow-md">
                <Shield className="w-6 h-6 text-white" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">
                Classification IA
              </h3>
              <p className="text-gray-600 leading-relaxed">
                Analyse automatique et classification instantanée selon les catégories EU AI Act : haut risque, risque limité, risque minimal.
              </p>
            </div>

            {/* Feature 2 */}
            <div className="group p-8 bg-white/70 border border-gray-200 rounded-2xl hover:border-blue-300 transition-all duration-300 backdrop-blur-sm shadow-lg hover:shadow-xl">
              <div className="w-12 h-12 bg-gradient-to-r from-blue-500 to-cyan-500 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform shadow-md">
                <FileText className="w-6 h-6 text-white" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">
                Documentation intelligente
              </h3>
              <p className="text-gray-600 leading-relaxed">
                Génération automatique de toute la documentation technique : évaluations, mesures de mitigation, instructions d'utilisation.
              </p>
            </div>

            {/* Feature 3 */}
            <div className="group p-8 bg-white/70 border border-gray-200 rounded-2xl hover:border-green-300 transition-all duration-300 backdrop-blur-sm shadow-lg hover:shadow-xl">
              <div className="w-12 h-12 bg-gradient-to-r from-green-500 to-emerald-500 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform shadow-md">
                <BarChart3 className="w-6 h-6 text-white" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">
                Détection de biais
              </h3>
              <p className="text-gray-600 leading-relaxed">
                Intelligence artificielle avancée pour détecter automatiquement les biais et proposer des améliorations concrètes.
              </p>
            </div>

            {/* Feature 4 */}
            <div className="group p-8 bg-white/70 border border-gray-200 rounded-2xl hover:border-orange-300 transition-all duration-300 backdrop-blur-sm shadow-lg hover:shadow-xl">
              <div className="w-12 h-12 bg-gradient-to-r from-orange-500 to-red-500 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform shadow-md">
                <Zap className="w-6 h-6 text-white" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">
                Monitoring temps réel
              </h3>
              <p className="text-gray-600 leading-relaxed">
                Surveillance continue de vos systèmes avec alertes intelligentes en cas de dérive de conformité ou de performance.
              </p>
            </div>

            {/* Feature 5 */}
            <div className="group p-8 bg-white/70 border border-gray-200 rounded-2xl hover:border-yellow-300 transition-all duration-300 backdrop-blur-sm shadow-lg hover:shadow-xl">
              <div className="w-12 h-12 bg-gradient-to-r from-yellow-500 to-orange-500 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform shadow-md">
                <Star className="w-6 h-6 text-white" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">
                Validation juridique
              </h3>
              <p className="text-gray-600 leading-relaxed">
                Certification de votre conformité par nos experts juridiques spécialisés en droit européen de l'intelligence artificielle.
              </p>
            </div>

            {/* Feature 6 */}
            <div className="group p-8 bg-white/70 border border-gray-200 rounded-2xl hover:border-cyan-300 transition-all duration-300 backdrop-blur-sm shadow-lg hover:shadow-xl">
              <div className="w-12 h-12 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform shadow-md">
                <MessageCircle className="w-6 h-6 text-white" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">
                Support expert
              </h3>
              <p className="text-gray-600 leading-relaxed">
                Accompagnement personnalisé par nos experts en conformité IA et assistance technique 24/7.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="relative py-20 px-6">
        <div className="max-w-4xl mx-auto text-center">
          <div className="p-12 bg-gradient-to-r from-purple-100/50 to-blue-100/50 border border-purple-200/50 rounded-3xl backdrop-blur-xl shadow-xl">
            <h2 className="text-4xl md:text-5xl font-bold mb-6 text-gray-900">
              Transformez vos obligations
              <br />
              <span className="bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">
                en avantage concurrentiel
              </span>
            </h2>
            <p className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto leading-relaxed">
              Découvrez comment ConforMind peut révolutionner votre approche de la conformité EU AI Act. 
              Démonstration personnalisée avec nos experts.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <button className="bg-gradient-to-r from-purple-500 to-blue-500 text-white px-8 py-4 rounded-xl text-lg font-medium hover:shadow-2xl hover:shadow-purple-500/25 transition-all duration-300 flex items-center justify-center gap-2 group">
                <Sparkles className="w-5 h-5" />
                Démonstration gratuite
                <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
              </button>
              <button className="border border-gray-300 text-gray-700 px-8 py-4 rounded-xl text-lg font-medium hover:border-purple-300 hover:text-purple-700 transition-all duration-300">
                Parler à un expert
              </button>
            </div>
            <p className="text-sm text-gray-500 mt-6">
              Sans engagement • Support en français • Démo de 30 minutes
            </p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="relative py-12 px-6 border-t border-gray-200">
        <div className="max-w-7xl mx-auto">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="flex items-center gap-2 mb-4 md:mb-0">
              <div className="w-8 h-8 bg-gradient-to-r from-purple-500 to-blue-500 rounded-lg flex items-center justify-center">
                <Sparkles className="w-5 h-5 text-white" />
              </div>
              <div>
                <span className="text-xl font-bold bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">
                  ConforMind
                </span>
                <p className="text-gray-500 text-sm">L'IA au service de la conformité IA</p>
              </div>
            </div>
            <div className="flex items-center gap-8 text-sm text-gray-500">
              <a href="#" className="hover:text-gray-900 transition-colors">Confidentialité</a>
              <a href="#" className="hover:text-gray-900 transition-colors">Conditions</a>
              <a href="#" className="hover:text-gray-900 transition-colors">Contact</a>
            </div>
          </div>
          <div className="mt-8 pt-8 border-t border-gray-200 text-center text-gray-400 text-sm">
            © 2025 ConforMind. Tous droits réservés.
          </div>
        </div>
      </footer>

      {/* Chatbot Placeholder */}
      <div className="fixed bottom-6 right-6 z-40">
        <div className="bg-white/90 backdrop-blur-sm border-2 border-dashed border-gray-300 rounded-2xl p-6 shadow-lg max-w-xs">
          <div className="flex items-center gap-3 mb-3">
            <div className="w-10 h-10 bg-gradient-to-r from-purple-500 to-blue-500 rounded-full flex items-center justify-center">
              <MessageCircle className="w-5 h-5 text-white" />
            </div>
            <div>
              <div className="font-medium text-gray-900 text-sm">Chatbot IA</div>
              <div className="text-xs text-gray-500">Futur emplacement</div>
            </div>
          </div>
          <p className="text-xs text-gray-600 text-center">
            Interface de chat intelligente sera intégrée ici
          </p>
        </div>
      </div>
    </div>
  );
};

export default LandingPage;