# ============================================================================
# EXTRACT Q&A PAIRS FROM TRANSCRIPTS
# ============================================================================

import re
import glob

def extract_qa_from_transcript(transcript_file):
    """
    Extract Q&A pairs from a single transcript.
    Returns list of Q&A dictionaries.
    """
    
    with open(transcript_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get video ID
    video_id_match = re.search(r'VIDEO_ID: (.+)', content)
    video_id = video_id_match.group(1) if video_id_match else "unknown"
    
    # Get source
    source_match = re.search(r'SOURCE: (.+)', content)
    source = source_match.group(1) if source_match else "unknown"
    
    # Get full transcript (without timestamps for easier reading)
    if "FULL TRANSCRIPT:" in content:
        full_text = content.split("FULL TRANSCRIPT:")[1].split("TIMESTAMPED SEGMENTS:")[0].strip()
    else:
        full_text = content
    
    # For now, return the full transcript for manual segmentation
    # You'll manually identify Q&A boundaries
    
    qa_pair = {
        'source': source,
        'video_id': video_id,
        'full_transcript': full_text,
        'transcript_file': transcript_file
    }
    
    return qa_pair


def create_qa_extraction_file():
    """
    Create a file with all transcripts ready for Q&A extraction.
    """
    
    print("="*80)
    print("🔍 EXTRACTING TRANSCRIPTS FOR Q&A IDENTIFICATION")
    print("="*80)
    
    # Get all transcript files
    youtube_files = glob.glob("transcripts/youtube/*.txt")
    interviewingio_files = glob.glob("transcripts/interviewingio/*.txt")
    
    all_files = youtube_files + interviewingio_files
    
    print(f"📊 Found {len(all_files)} transcripts")
    print(f"   YouTube: {len(youtube_files)}")
    print(f"   interviewing.io: {len(interviewingio_files)}")
    
    # Extract and save
    qa_data = []
    
    for i, file in enumerate(all_files[:5], 1):  # Start with 5 for testing
        print(f"\n[{i}/5] Processing: {file}")
        qa_pair = extract_qa_from_transcript(file)
        qa_data.append(qa_pair)
    
    # Save to JSON for easy viewing
    import json
    with open('transcripts_for_qa_extraction.json', 'w', encoding='utf-8') as f:
        json.dump(qa_data, f, indent=2, ensure_ascii=False)
    
    print("\n" + "="*80)
    print("✅ SAVED: transcripts_for_qa_extraction.json")
    print("="*80)
    print("\nNext step: Manually identify Q&A pairs in each transcript")
    
    return qa_data


def show_sample_transcript():
    """
    Show a sample transcript to help identify Q&A structure.
    """
    
    files = glob.glob("transcripts/youtube/*.txt")
    
    if files:
        print("="*80)
        print("📄 SAMPLE TRANSCRIPT (First 2000 characters)")
        print("="*80)
        
        with open(files[0], 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Get full transcript section
            if "FULL TRANSCRIPT:" in content:
                transcript = content.split("FULL TRANSCRIPT:")[1].split("TIMESTAMPED SEGMENTS:")[0]
                print(transcript[:2000])
                print("\n... (truncated)")
            else:
                print(content[:2000])
                print("\n... (truncated)")
        
        print("\n" + "="*80)
        print("👆 Look for patterns like:")
        print("   - Interviewer asking questions")
        print("   - Candidate responding")
        print("   - Topic changes")
        print("="*80)
    else:
        print("❌ No transcripts found")


# Run extraction
qa_data = create_qa_extraction_file()

# Show sample
show_sample_transcript()