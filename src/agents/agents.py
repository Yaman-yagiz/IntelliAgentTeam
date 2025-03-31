import sys
from pathlib import Path
from typing import Dict, Optional

import google.generativeai as genai
from src.core.config import GEMINI_API_KEY, INSTRUCTION_DIR

# API anahtarını ayarla
genai.configure(api_key=GEMINI_API_KEY)


def load_project_description(file_path: str) -> str:
    """
    Proje açıklama dosyasını yükler.
    
    Args:
        file_path: Proje açıklama dosyasının yolu
        
    Returns:
        Proje açıklaması metni
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except Exception as e:
        raise Exception(f"Proje açıklama dosyası yüklenirken hata oluştu: {str(e)}")


class Agent:
    """LLM tabanlı bir AI ajanı."""
    
    def __init__(self, name: str, role: str, instruction_file: Optional[str] = None):
        """
        Args:
            name: Ajanın adı
            role: Ajanın rolü
            instruction_file: Ajanın talimatlarını içeren dosya 
        """
        self.name = name
        self.role = role
        self.instructions = ""
        
        # Talimat dosyası verildiyse yükle
        if instruction_file:
            try:
                instruction_path = Path(INSTRUCTION_DIR) / instruction_file
                with open(instruction_path, 'r', encoding='utf-8') as f:
                    self.instructions = f.read().strip()
            except Exception as e:
                print(f"Uyarı: {instruction_file} dosyası yüklenirken hata oluştu: {str(e)}")
    
    def query(self, prompt: str) -> str:
        """
        Ajana bir soru sorar ve yanıt alır.
        
        Args:
            prompt: Ajana sorulacak soru/istek
            
        Returns:
            Ajanın yanıtı
        """
        try:
            model = genai.GenerativeModel('gemini-2.0-flash-exp')
            
            # Talimatları ve prompu birleştir
            full_prompt = f"{self.instructions}\n\n{prompt}" if self.instructions else prompt
            
            response = model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            error_msg = f"{self.name} ajanından yanıt alınırken hata oluştu: {str(e)}"
            print(error_msg, file=sys.stderr)
            return f"[Hata: {error_msg}]"


class ProjectTeam:
    """Proje ekibi sınıfı."""
    
    def __init__(self):
        """Proje ekibini oluşturur."""
        self.project_manager = None
        self.ux_designer = None 
        self.software_architect = None
        self.team_leader = None
    
    def initialize_agents(self):
        """Tüm ajanları başlatır."""
        self.project_manager = Agent(
            name="Proje Yöneticisi",
            role="Proje planlama ve yönetim uzmanı",
            instruction_file="project_manager_instructions.txt"
        )
        
        self.ux_designer = Agent(
            name="UX Tasarımcısı",
            role="Kullanıcı deneyimi ve arayüz tasarım uzmanı",
            instruction_file="ux_designer_instructions.txt"
        )
        
        self.software_architect = Agent(
            name="Yazılım Mimarı",
            role="Teknik mimari ve yazılım geliştirme uzmanı",
            instruction_file="software_architect_instructions.txt"
        )
        
        self.team_leader = Agent(
            name="Ekip Lideri",
            role="Ekip koordinasyonu ve genel proje yönetimi",
            instruction_file="team_leader_instructions.txt"
        )
    
    def simulate_discussion(self, project_description: str) -> Dict[str, str]:
        """
        Ajanlar arasında bir tartışma simülasyonu yapar.
        
        Args:
            project_description: Proje açıklaması
            
        Returns:
            Her ajanın yanıtlarını içeren sözlük
        """
        responses = {}
        
        # Tüm gerekli ajanların başlatıldığından emin ol
        if not all([self.project_manager, self.ux_designer, self.software_architect]):
            raise Exception("Tüm ajanlar başlatılmadı.")
        
        # Proje Yöneticisi'nin görüşünü al
        print("🔄 Proje Yöneticisi analiz yapıyor...")
        pm_prompt = f"""
        Proje Açıklaması:
        {project_description}
        
        Lütfen bu proje için detaylı bir proje yönetim planı oluşturun.
        """
        responses['project_manager'] = self.project_manager.query(pm_prompt)
        print("✅ Proje Yöneticisi analizini tamamladı.\n")
        
        # UX Tasarımcı'nın görüşünü al
        print("🔄 UX Tasarımcısı analiz yapıyor...")
        ux_prompt = f"""
        Proje Açıklaması:
        {project_description}
        
        Proje Yöneticisi'nin Görüşleri:
        {responses['project_manager']}
        
        Lütfen bu proje için detaylı bir UX/UI tasarım stratejisi oluşturun.
        """
        responses['ux_designer'] = self.ux_designer.query(ux_prompt)
        print("✅ UX Tasarımcısı analizini tamamladı.\n")
        
        # Yazılım Mimarı'nın görüşünü al
        print("🔄 Yazılım Mimarı analiz yapıyor...")
        arch_prompt = f"""
        Proje Açıklaması:
        {project_description}
        
        Proje Yöneticisi'nin Görüşleri:
        {responses['project_manager']}
        
        UX Tasarımcısı'nın Görüşleri:
        {responses['ux_designer']}
        
        Lütfen bu proje için detaylı bir teknik mimari planı oluşturun.
        """
        responses['software_architect'] = self.software_architect.query(arch_prompt)
        print("✅ Yazılım Mimarı analizini tamamladı.")
        
        return responses
    
    def generate_executive_summary(self, project_description: str, responses: Dict[str, str]) -> str:
        """
        Ekip lideri tarafından bir yönetici özeti oluşturur.
        
        Args:
            project_description: Proje açıklaması
            responses: Diğer ajanların yanıtları
            
        Returns:
            Ekip liderinin özet yanıtı
        """
        if not self.team_leader:
            raise Exception("Ekip lideri ajanı başlatılmadı.")
        
        print("\n🔄 Ekip Lideri yönetici özeti hazırlıyor...")
        
        team_leader_prompt = f"""
        Proje Açıklaması:
        {project_description}
        
        Proje Yöneticisi'nin Raporu:
        {responses['project_manager']}
        
        UX Tasarımcısı'nın Raporu:
        {responses['ux_designer']}
        
        Yazılım Mimarı'nın Raporu:
        {responses['software_architect']}
        
        Lütfen bu proje için tüm uzmanların görüşlerini dikkate alarak kapsamlı bir yönetici özeti oluşturun.
        """
        
        response = self.team_leader.query(team_leader_prompt)
        print("✅ Yönetici özeti hazırlandı.")
        
        # Yanıt string değilse string'e dönüştür
        if not isinstance(response, str):
            response = str(response)
            
        return response 