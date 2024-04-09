from met import Met

met = Met()

while met.running:
    met.event_handle()

    met.update()
    
    met.flip()
    met.tick()

met.quit()
