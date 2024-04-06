from met import Met

met = Met()

while met.running:
    met.event_handle()

    if met.should_i_click():
        met.click()
    
    met.flip()
    met.tick()

met.quit()
