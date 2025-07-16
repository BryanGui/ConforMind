import Header from "@/components/layout/Header";
import HeroSection from "@/components/landing/HeroSection";
import Features from "@/components/landing/Features";
import CTASection from "@/components/landing/CTASection";
import Footer from "@/components/layout/Footer";

export default function LandingPage() {
  return (
    <main className="bg-black text-white">
      <Header />
      <HeroSection />
      <Features />
      <CTASection />
      <Footer />
    </main>
  );
}