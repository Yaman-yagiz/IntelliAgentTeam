import sys
from src.core.config import setup_environment, PROJECT_DESC_PATH
from src.agents import ProjectTeam, load_project_description
from src.utils import extract_project_name


def main():
    """Ana program fonksiyonu."""
    print("🚀 AI Tabanlı Proje Planlama Sistemi başlatılıyor...\n")
    
    # Çevre değişkenlerini ayarla
    setup_environment()
    
    try:
        # Proje açıklamasını yükle
        project_description = load_project_description(str(PROJECT_DESC_PATH))
        project_name = extract_project_name(project_description)
        print(f"📋 Proje açıklaması yüklendi: {project_name}\n")
        
        # Proje ekibini oluştur
        team = ProjectTeam()
        team.initialize_agents()
        
        # Uzman raporlarını oluştur
        responses = team.simulate_discussion(project_description)
        
        # Ekip lideri özeti
        team_leader_response = team.generate_executive_summary(project_description, responses)
        responses['team_leader'] = team_leader_response
        
        # Sonuçları terminalde göster
        print("\n" + "="*80)
        print(f"📊 PROJE YÖNETİMİ PLANI\n")
        print(responses['project_manager'])
        
        print("\n" + "="*80)
        print(f"🎨 UX/UI TASARIM STRATEJİSİ\n")
        print(responses['ux_designer'])
        
        print("\n" + "="*80)
        print(f"💻 TEKNİK MİMARİ PLANI\n")
        print(responses['software_architect'])
        
        print("\n" + "="*80)
        print(f"📝 YÖNETİCİ ÖZETİ\n")
        print(responses['team_leader'])
        print("="*80)
        
        print("\n✅ İşlem tamamlandı!")
        
    except Exception as e:
        print(f"❌ Hata: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
